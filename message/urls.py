from django.conf.urls import url

from .views import all_private_messages_between_two_users


app_name = 'message' # namespace for this app

urlpatterns = [
    url(r'^(?P<another_user_id>\d+)/$', all_private_messages_between_two_users, name='all_private_messages_between_two_users'),
]
