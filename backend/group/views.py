from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from message.models import GroupMessage
from .models import Group
from .forms import MessageCreateForm
from .serializers import GroupMessageSerializer


@api_view(['GET'])
@login_required
def group_messages(request, group_slug):
    messages = GroupMessage.objects.filter(group__slug=group_slug)
    serialized_messages = GroupMessageSerializer(messages, many=True)
    context = {'messages': serialized_messages.data}
    return Response(context)

@api_view(['GET'])
def group_single_message_detail(request, group_slug, message_id):
    messages = GroupMessage.objects.filter(group__slug=group_slug)
    message = messages.filter(id=message_id).first()
    if not message:
        raise Http404
    serialized_message = GroupMessageSerializer(message)
    context = {'message': serialized_message.data}
    return Response(context)


def group_single_message_create(request, group_slug):
    if request.method == 'POST':
        message_form = MessageCreateForm(request.POST)
        if message_form.is_valid():
            message_content = message_form.cleaned_data.get('content')
            new_message = GroupMessage(content=message_content)
            new_message.sender = request.user
            new_message.group = get_object_or_404(Group, slug=group_slug)
            new_message.save()
    else:
        message_form = MessageCreateForm()
    return render(request, 'group_single_message_create.html', {'message_form': message_form})
