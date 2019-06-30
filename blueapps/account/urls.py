# -*- coding: utf-8 -*-
from django.conf.urls import url

from blueapps.account import views

app_name = 'account'

urlpatterns = [
    url(r'^login_out/$', views.login_out, name="login_out"),
]
