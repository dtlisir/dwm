# -*- coding: utf-8 -*-

from django.conf.urls import url
from images import views

urlpatterns = (
    url(r'^image_list/$', views.image_list, name='image_list'),
)