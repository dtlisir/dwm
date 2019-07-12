import logging
from django.shortcuts import render
from django.http import JsonResponse
from .models import HostGroup, HostNode
from syslogs.models import Log
from common.docker_api import get_docker_info


# 主机相关
def node_list(request):
    return render(request, 'hosts/node_list.html')


def test_node_conn(request):
    node_url = request.GET.get('node_url')
    resp = get_docker_info(node_url)
    return JsonResponse({'result': resp['result']})


def node_create(request):
    groups = HostGroup.objects.values('id', 'name')
    return render(request, 'hosts/node_create.html', {'groups': groups})


def post_create_node(request):
    node_name = request.POST.get('node_name')
    node_url = request.POST.get('node_url')
    node_ip = request.POST.get('node_ip')
    node_group = request.POST.get('node_group')
    node_comment = request.POST.get('node_comment')
    user = request.user.username
    try:
        if HostNode.objects.filter(name=node_name):
            return  JsonResponse({'result': False, 'message': '主机名称已经存在，请重新填写'})
        if HostNode.objects.filter(url=node_url):
            return  JsonResponse({'result': False, 'message': '主机URL已经存在，请重新填写'})
        group = None
        if node_group:
            group = HostGroup.objects.get(id=node_group)
        resp = get_docker_info(node_url)
        if not resp['result']:
            return  JsonResponse({'result': False, 'message': '主机URL连接失败，请检查'})
        data = resp['data']
        HostNode.objects.create(
            name=node_name,
            url=node_url,
            ip=node_ip,
            group=group,
            created_by=user,
            comment=node_comment,
            os=data['OperatingSystem'],
            os_arch=data['Architecture'],
            cpu_count=data['NCPU'],
            memory=data['MemTotal'],
            active=True,
            c_running=data['ContainersRunning'],
            c_paused=data['ContainersPaused'],
            c_stopped=data['ContainersStopped'],
            d_version=data['ServerVersion'],
            c_count=data['Containers'],
            i_count=data['Images']
        )
        Log.objects.create(
            user=user,
            type='HOST',
            action='CREATE',
            state=True,
            content='主机添加成功'
        )
        return  JsonResponse({'result': True, 'message': '主机添加成功'})
    except Exception as e:
        Log.objects.create(
            user=user,
            type='HOST',
            action='CREATE',
            state=False,
            content='主机添加失败，原因：%s' % (str(e))
        )
        return JsonResponse({'result': False, 'message': '主机添加失败'})


def get_node_list(request):
    nodes = HostNode.objects.all()
    data = []
    if nodes:
        data = [node.to_dict() for node in nodes]
    return JsonResponse({'data': data})


def node_del(request):
    id = int(request.GET.get('id'))
    user = request.user.username
    try:
        HostNode.objects.filter(id=id).delete()
        Log.objects.create(
            user=user,
            type='HOST',
            action='DELETE',
            state=True,
            content='主机删除成功'
        )
        return JsonResponse({'result': True})
    except Exception as e:
        Log.objects.create(
            user=user,
            type='HOST',
            action='DELETE',
            state=False,
            content='主机删除失败，原因：%s' % (str(e))
        )
        return JsonResponse({'result': False})


def node_edit(request, pk):
    groups = HostGroup.objects.values('id', 'name')
    node = HostNode.objects.get(id=pk)
    return render(request, 'hosts/node_edit.html', {'node': node, 'groups': groups})


def post_edit_node(request):
    node_id = request.POST.get('node_id')
    node_name = request.POST.get('node_name')
    node_url = request.POST.get('node_url')
    node_ip = request.POST.get('node_ip')
    node_group = request.POST.get('node_group')
    node_comment = request.POST.get('node_comment')
    user = request.user.username
    try:
        if HostNode.objects.filter(name=node_name):
            return  JsonResponse({'result': False, 'message': '主机名称已经存在，请重新填写'})
        if HostNode.objects.filter(url=node_url):
            return  JsonResponse({'result': False, 'message': '主机URL已经存在，请重新填写'})
        group = None
        if node_group:
            group = HostGroup.objects.get(id=node_group)
        resp = get_docker_info(node_url)
        if not resp['result']:
            return  JsonResponse({'result': False, 'message': '主机URL连接失败，请检查'})
        node = HostNode.objects.get(id=node_id)
        node.name = node_name
        node.url = node.url
        node.ip = node_ip
        node.group = group
        node.comment = node_comment
        node.save()
        Log.objects.create(
            user=user,
            type='HOST',
            action='UPDATE',
            state=True,
            content='主机修改成功'
        )
        return  JsonResponse({'result': True, 'message': '主机修改成功'})
    except Exception as e:
        Log.objects.create(
            user=user,
            type='HOST',
            action='UPDATE',
            state=False,
            content='主机修改失败，原因：%s' % (str(e))
        )
        return JsonResponse({'result': False, 'message': '主机修改失败'})


def node_detail(request, pk):
    node = HostNode.objects.get(id=pk)
    return render(request, 'hosts/node_detail.html', {'node': node})


# 组相关
def group_list(request):
    return render(request, 'hosts/group_list.html')


def get_group_list(request):
    groups = HostGroup.objects.all()
    data = []
    if groups:
        data = [group.to_dict() for group in groups]
    return JsonResponse({'data': data})


def group_create(request):
    return render(request, 'hosts/group_create.html')


def post_create_group(request):
    group_name = request.POST.get('group_name')
    group_comment = request.POST.get('group_comment')
    user = request.user.username
    try:
        if HostGroup.objects.filter(name=group_name):
            return  JsonResponse({'result': False, 'message': '组名称已经存在，请重新填写'})
        HostNode.objects.create(
            name=group_name,
            created_by=user,
            comment=group_comment,
        )
        Log.objects.create(
            user=user,
            type='GROUP',
            action='CREATE',
            state=True,
            content='组添加成功'
        )
        return  JsonResponse({'result': True, 'message': '组添加成功'})
    except Exception as e:
        Log.objects.create(
            user=user,
            type='GROUP',
            action='CREATE',
            state=False,
            content='组添加失败，原因：%s' % (str(e))
        )
        return JsonResponse({'result': False, 'message': '组添加失败'})


def group_edit(request, pk):
    group = HostGroup.objects.get(id=pk)
    return render(request, 'hosts/group_edit.html', {'group': group})


def post_edit_group(request):
    group_id = request.POST.get('group_id')
    group_name = request.POST.get('group_name')
    group_comment = request.POST.get('group_comment')
    user = request.user.username
    try:
        if HostGroup.objects.filter(name=group_name):
            return  JsonResponse({'result': False, 'message': '组名称已经存在，请重新填写'})
        group = HostGroup.objects.get(id=group_id)
        group.name = group_name
        group.comment = group_comment
        group.save()
        Log.objects.create(
            user=user,
            type='GROUP',
            action='UPDATE',
            state=True,
            content='组修改成功'
        )
        return  JsonResponse({'result': True, 'message': '组修改成功'})
    except Exception as e:
        Log.objects.create(
            user=user,
            type='GROUP',
            action='UPDATE',
            state=False,
            content='组修改失败，原因：%s' % (str(e))
        )
        return JsonResponse({'result': False, 'message': '组修改失败'})


def group_del(request):
    id = int(request.GET.get('id'))
    user = request.user.username
    try:
        HostGroup.objects.filter(id=id).delete()
        Log.objects.create(
            user=user,
            type='GROUP',
            action='DELETE',
            state=True,
            content='组删除成功'
        )
        return JsonResponse({'result': True})
    except Exception as e:
        Log.objects.create(
            user=user,
            type='GROUP',
            action='DELETE',
            state=False,
            content='组删除失败，原因：%s' % (str(e))
        )
        return JsonResponse({'result': False})


