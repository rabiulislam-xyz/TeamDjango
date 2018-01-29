from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from message.models import PrivateMessage
from .serializers import PrivateMessageSerializer


@api_view(['GET'])
def all_private_messages_between_two_users(request, another_user_id):
    current_user = request.user
    another_user = get_object_or_404(User, id=another_user_id)

    # retrieve sent messages and received messages between these tow users
    messages = PrivateMessage.objects.filter((Q(sender=current_user) & Q(receiver=another_user)) |
                                             (Q(receiver=current_user) & Q(sender=another_user))).distinct()

    serialized_messages = PrivateMessageSerializer(messages, many=True)
    context = {
        'current_user': current_user.username,
        'another_user': another_user.username,
        'messages': serialized_messages.data
    }
    return Response(context)



# def all_private_messages_between_two_users(request, another_user_id):
#     current_user = request.user
#     another_user = get_object_or_404(User, id=another_user_id)
#
#     # retrieve sent messages and received messages between these two users
#     messages = PrivateMessage.objects.filter((Q(sender=current_user) & Q(receiver=another_user)) |
#                                              (Q(receiver=current_user) & Q(sender=another_user))).distinct()
#
#     context = {
#         'current_user': current_user,
#         'another_user': another_user,
#         'messages': messages
#     }
#     return render(request, 'all_private_messages_between_two_users.html', context)
