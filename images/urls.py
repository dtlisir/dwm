# -*- coding: utf-8 -*-

from django.conf.urls import url
from images import views

urlpatterns = (
    url(r'^image_list/(?P<pk>[0-9]+)/$', views.image_list, name='image_list'),
    url(r'^get_image_list/$', views.get_image_list, name='get_image_list'),
)