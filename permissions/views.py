# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import JsonResponse
from hosts.models import HostNode
from blueapps.account.models import User
from syslogs.models import Log


def user_list(request):
    if not request.user.is_superuser:
        return redirect('home:forbiden')
    return render(request, 'permissions/user_list.html')


def get_user_list(request):
    if not request.user.is_superuser:
        JsonResponse({'result': False, 'message': 'Permission denied'})
    users = User.objects.all()
    data = []
    for user in users:
        user_dict = {
            'name': user.username,
            'role': '管理员' if user.is_superuser else '普通用户',
            'nickname': user.nickname,
            'last_login': user.last_login.strftime("%Y-%m-%d %H:%M:%S"),
            'date_joined': user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
        }
        data.append(user_dict)
    return JsonResponse({'data': data})


def set_perm(request):
    if not request.user.is_superuser:
        return redirect('home:forbiden')
    users = User.objects.filter(is_superuser=0)
    nodes = HostNode.objects.all()
    return render(request, 'permissions/set_perm.html', {'nodes': nodes, 'users': users})


def get_node_users(request):
    if not request.user.is_superuser:
        JsonResponse({'result': False, 'message': 'Permission denied'})
    node_id = int(request.GET.get('node_id'))
    try:
        node = HostNode.objects.get(id=node_id)
        id_list = node.users.values('id')
        user_id_list = [ data['id'] for data in id_list]
        print(user_id_list)
        return JsonResponse({'data': user_id_list})
    except Exception as e:
        return JsonResponse({'data': []})


def post_perm_set(request):
    if not request.user.is_superuser:
        JsonResponse({'result': False, 'message': 'Permission denied'})
    user = request.user.username
    try:
        node_id = int(request.POST.get('node_id'))
        user_str = request.POST.get('user_str')
        user_id_list = user_str.split(',')
        node = HostNode.objects.get(id=node_id)
        users = User.objects.filter(id__in=user_id_list)
        for s_user in users:
            node.users.add(s_user)
        node.save()
        Log.objects.create(
            user=user,
            type='PERMISSION',
            action='AUTH',
            state=True,
            content='用户授权成功'
        )
        return  JsonResponse({'result': True, 'message': '用户授权成功'})
    except Exception as e:
        Log.objects.create(
            user=user,
            type='PERMISSION',
            action='AUTH',
            state=False,
            content='用户授权失败，原因：%s' % (str(e))
        )
        return JsonResponse({'result': False, 'message': '用户授权失败'})
