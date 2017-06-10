# urls.py ---
#
# Filename: urls.py
# Description:
#
# Author:
# Created: Sat Jun 10 00:38:35 2017 (-0500)
from django.conf.urls import patterns, url

from .views import (ProfileView, MyProfileView, ProfileUpdateView)



urlpatterns = patterns(
    '',

    url(r'^profile/$',
        MyProfileView.as_view(),
        name="view_profile"),

    url(r'^profile/(?P<username>.+)/$',
        ProfileView.as_view(),
        name="view_profile"),

    url(r'^profile-edit/$',
        ProfileUpdateView.as_view(),
        name="update_profile"),
)
