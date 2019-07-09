# -*- coding: utf-8 -*-

from django.conf.urls import url
from users import views

urlpatterns = (
    url(r'^login_list/$', views.login_list, name='login_list'),
    url(r'^ops_list/$', views.ops_list, name='ops_list'),
    url(r'^get_user_list/$', views.get_user_list, name='get_user_list'),
)