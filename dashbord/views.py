# -*- coding: utf-8 -*-
from django.shortcuts import render
from hosts.models import HostNode
from blueapps.account.models import User
from django.db.models.aggregates import Sum


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def index(request):
    host_count = HostNode.objects.all().count()
    user_count = User.objects.all().count()
    container_totle = HostNode.objects.all().aggregate(totles=Sum('c_count'))
    container_count = container_totle['totles']
    image_totle = HostNode.objects.all().aggregate(totles=Sum('i_count'))
    image_count = image_totle['totles']
    context = {
        'host_count': host_count,
        'user_count': user_count,
        'container_count': container_count,
        'image_count': image_count,
    }
    return render(request, 'dashbord/index.html', context)
