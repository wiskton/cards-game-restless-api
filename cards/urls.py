"""cards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import restless

from users.views import UserList, UserDetail, FriendList, FriendDetail, SocialNetworkList, SocialNetworkDetail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^login/$', restless.auth.AuthenticateEndpoint.as_view()),
    url(r'^users/$', UserList.as_view(), name='user_list'),
    url(r'^users/(?P<pk>\d+)$', UserDetail.as_view(), name='user_detail'),

    url(r'^friends/$', FriendList.as_view(), name='friend_list'),
    url(r'^friends/(?P<pk>\d+)$', FriendDetail.as_view(), name='friend_detail'),


    url(r'^socialnetworks/$', SocialNetworkList.as_view(), name='socialnetwork_list'),
    url(r'^socialnetworks/(?P<pk>\d+)$', SocialNetworkDetail.as_view(), name='socialnetwork_detail'),

    # url(r'^friends/(?P<id_user>\d+)$', FriendList.as_view(), name='friend_list'),
    # url(r'^social-networks/(?P<id_user>\d+)$', SocialNetworksList.as_view(), name='social_networks_list'),

]
