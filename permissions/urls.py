# -*- coding: utf-8 -*-

from django.conf.urls import url
from permissions import views

urlpatterns = (
    url(r'^permission_list/$', views.permission_list, name='permission_list'),
)