# -*- coding: utf-8 -*-

from django.conf.urls import url
from syslogs import views

urlpatterns = (
    url(r'^user_list/$', views.user_list, name='user_list'),
    url(r'^ops_list/$', views.ops_list, name='ops_list'),
    url(r'^get_user_list/$', views.get_user_list, name='get_user_list'),
)