# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from hosts.models import HostNode
from blueapps.account.models import User
from django.db.models.aggregates import Sum


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def index(request):
    if not request.user.is_superuser:
        return redirect('home:index_user')
    nodes = HostNode.objects.all()
    host_count = nodes.count()
    user_count = User.objects.all().count()
    container_totle = nodes.aggregate(totles=Sum('c_count'))
    container_running = nodes.aggregate(totles=Sum('c_running'))
    container_stopped = nodes.aggregate(totles=Sum('c_stopped'))
    container_paused = nodes.aggregate(totles=Sum('c_paused'))
    container_count = container_totle['totles']
    c_running_count = container_running['totles']
    c_stopped_count = container_stopped['totles']
    c_paused_count = container_paused['totles']
    image_totle = nodes.aggregate(totles=Sum('i_count'))
    image_count = image_totle['totles']
    node_container_top5 = nodes.order_by('-c_count')[:5]
    ip_list = [ node.url.split(':')[0] for node in node_container_top5]
    c_count_list = [ node.c_count for node in node_container_top5]
    i_count_list = [ node.i_count for node in node_container_top5]

    context = {
        'nodes': nodes,
        'host_count': host_count,
        'user_count': user_count,
        'container_count': container_count,
        'image_count': image_count,
        'ip_list': ip_list,
        'c_count_list': c_count_list,
        'i_count_list': i_count_list,
        'c_running_count': c_running_count,
        'c_stopped_count': c_stopped_count,
        'c_paused_count': c_paused_count,
    }
    return render(request, 'home/index.html', context)


def index_user(request):
    user = request.user.username
    nodes = HostNode.objects.filter(users__username=user)
    return render(request, 'home/index_user.html', {'nodes': nodes})


def forbiden(request):
    return render(request, 'home/forbiden.html')