# -*- coding: utf-8 -*-

from django.conf.urls import url
from permissions import views


urlpatterns = (
    url(r'^user_list/$', views.user_list, name='user_list'),
    url(r'^get_user_list/$', views.get_user_list, name='get_user_list'),

    url(r'^set_perm/$', views.set_perm, name='set_perm'),
    url(r'^get_node_users/$', views.get_node_users, name='get_node_users'),
    url(r'^post_perm_set/$', views.post_perm_set, name='post_perm_set'),
)