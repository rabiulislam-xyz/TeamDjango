from django.conf.urls import url

from .views import home, profile, update_profile


app_name = 'account' # namespace for this app

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^update/$', update_profile, name='update_profile'),
]
