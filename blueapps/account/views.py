# -*- coding: utf-8 -*-
from urllib.parse import urlencode
from django.conf import settings
from django.shortcuts import  redirect
from django.contrib.auth import logout
from django.contrib.auth.views import redirect_to_login
from blueapps.account.decorators import login_exempt


@login_exempt
def login_out(request):
    logout(request)
    if 'HTTP_REFERER' in request.META:
        http_referer = request.META['HTTP_REFERER']
    else:
        http_referer = settings.SITE_URL
    login_url = "%s/login/?app_id=%s" % (settings.BK_URL, settings.APP_CODE)
    return redirect_to_login(http_referer, login_url, 'c_url')
