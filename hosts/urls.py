# -*- coding: utf-8 -*-

from django.conf.urls import url
from hosts import views

urlpatterns = (
    url(r'^node_list/$', views.node_list, name='node_list'),
    url(r'^add_node/$', views.add_node, name='add_node'),
    url(r'^add_group/$', views.add_group, name='add_group'),

)
