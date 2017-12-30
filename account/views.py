from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db import transaction
from django.urls import reverse

from rest_framework.decorators import api_view
from rest_framework.views import Response

from group.serializers import GroupSerializer
from .serializers import UserSerializer

from .forms import UserForm, ProfileForm
from message.models import PrivateMessage
from group.models import Group

@login_required
def home(request):
    user = request.user  # current user

    # retrieve sent messages and received messages
    messages = PrivateMessage.objects.filter(Q(sender=user) | Q(receiver=user)).distinct().order_by('-created_at')
    groups = user.subscribed_groups.all()
    context = {
        'user': user,
        'messages': messages,
        'groups': groups
    }
    return render(request, 'account/home.html', context)


@api_view(['GET', 'POST'])
@login_required
def profile(request):
    user = UserSerializer(request.user)
    members = User.objects.all()
    serialized_members = UserSerializer(members, many=True, context={'request': request})
    context = {
        'user':user.data,
        'members': serialized_members.data
    }
    return Response(context)


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # get current user and add updated info to
            # User and its Profile model
            current_user = User.objects.get(pk=request.user.pk)

            # adding info to User model
            current_user.first_name = user_form.cleaned_data.get('first_name')
            current_user.last_name = user_form.cleaned_data.get('last_name')
            current_user.email = user_form.cleaned_data.get('email')

            # adding info to user's Profile model
            current_user.profile.photo = profile_form.cleaned_data.get('photo')
            current_user.profile.website = profile_form.cleaned_data.get('website')
            current_user.profile.location = profile_form.cleaned_data.get('location')

            current_user.save()
            return redirect(reverse('account:home'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, 'account/profile_update_form.html', context)

