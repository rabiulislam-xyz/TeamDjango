from django.conf.urls import url

from .views import group_messages, group_single_message_detail, group_single_message_create


app_name = 'group' # namespace for this app

urlpatterns = [
    url(r'^(?P<group_slug>[\w-]+)/$', group_messages, name='group_messages'),
    url(r'^(?P<group_slug>[\w-]+)/(?P<message_id>\d+)/$', group_single_message_detail, name='group_single_message_detail'),
    url(r'^(?P<group_slug>[\w-]+)/new/$', group_single_message_create, name='group_single_message_create'),
]
