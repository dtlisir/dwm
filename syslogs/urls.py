# -*- coding: utf-8 -*-

from django.conf.urls import url
from syslogs import views

urlpatterns = (
    url(r'^ops_list/$', views.ops_list, name='ops_list'),
    url(r'^get_ops_list/$', views.get_ops_list, name='get_ops_list'),
    url(r'^get_log_clear/$', views.get_log_clear, name='get_log_clear'),
)