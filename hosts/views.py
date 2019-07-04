import logging
from django.shortcuts import render
from django.http import JsonResponse
from .models import HostGroup, HostNode

logger = logging.getLogger('app')

# 节点相关
def node_list(request):
    return render(request, 'hosts/node_list.html')


def node_create(request):
    groups = HostGroup.objects.values('id', 'name')
    if request.method == 'GET':
        return render(request, 'hosts/node_create.html', {'groups': groups})
    elif request.method == 'POST':
        node_name = request.POST.get('node_name')
        node_url = request.POST.get('node_url')
        node_ip = request.POST.get('node_ip')
        group_id = request.POST.get('group_id')
        node_comment = request.POST.get('node_comment')
        user = request.user.username
        try:
            check_name = HostNode.objects.filter(name=node_name)
            if check_name:
                return render(request, 'hosts/node_create.html', {'groups': groups, 'error': '节点名称已经存在，请重新填写'})
            check_url = HostNode.objects.filter(node_url=node_url)
            if check_url:
                return render(request, 'hosts/node_create.html', {'groups': groups, 'error': '节点URL已经存在，请重新填写'})
            node_group = HostGroup.objects.get(id=group_id)
            HostNode.objects.create(
                name=node_name,
                node_url=node_url,
                ip=node_ip,
                group=node_group,
                created_by=user,
                comment=node_comment)
            return render(request, 'hosts/node_list.html')
        except Exception as e:
            return render(request, 'hosts/node_create.html', {'groups': groups, 'error': '节点创建失败，请检查'})


def get_node_list(request):
    nodes = HostNode.objects.all()
    data = []
    if nodes:
        data = [node.to_dict() for node in nodes]
    return JsonResponse({'data': data})


def node_del(request):
    id = int(request.GET.get('id'))
    try:
        HostNode.objects.filter(id=id).delete()
        return JsonResponse({'result': True})
    except Exception as e:
        return JsonResponse({'result': False})


def node_edit(request, pk):
    groups = HostGroup.objects.values('id', 'name')
    node = HostNode.objects.get(id=pk)
    if request.method == 'GET':
        if groups:
            return render(request, 'hosts/node_edit.html', {'node': node, 'groups': groups})
        else:
            return render(request, 'hosts/node_edit.html', {'node': node})
    elif request.method == 'POST':
        node_name = request.POST.get('node_name')
        node_url = request.POST.get('node_url')
        node_ip = request.POST.get('node_ip')
        group_id = request.POST.get('group_id')
        node_comment = request.POST.get('node_comment')
        try:
            if node_name != node.name:
                check_name = HostNode.objects.filter(name=node_name)
                if check_name:
                    return render(request, 'hosts/node_edit.html', {'node': node, 'groups': groups, 'error': '节点名称已经存在，请重新填写'})
                node.name = node_name
            if node_url != node.node_url:
                check_url = HostNode.objects.filter(node_url=node_url)
                if check_url:
                    return render(request, 'hosts/node_edit.html', {'node': node, 'groups': groups, 'error': '节点URL已经存在，请重新填写'})
                node.node_url = node_url
            node.ip=node_ip
            node_group = HostGroup.objects.get(id=group_id)
            if node_group:
                node.group=node_group
            node.comment=node_comment
            node.save()
            return render(request, 'hosts/node_list.html')
        except Exception as e:
            return render(request, 'hosts/node_edit.html', {'node': node, 'groups': groups, 'error': '节点编辑失败，请检查'})


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
    if request.method == 'GET':
        return render(request, 'hosts/group_create.html')
    elif request.method == 'POST':
        g_name = request.POST.get('g_name')
        g_comment = request.POST.get('g_comment')
        user = request.user.username
        try:
            check_name = HostNode.objects.filter(name=g_name)
            if check_name:
                return render(request, 'hosts/node_create.html', {'error': '组名称已经存在，请重新填写'})
            HostGroup.objects.create(name=g_name, created_by=user, comment=g_comment)
            return render(request, 'hosts/group_list.html')
        except Exception as e:
            return render(request, 'hosts/group_create.html', {'error': '组创建失败，请检查'})


def group_edit(request, pk):
    group = HostGroup.objects.get(id=pk)
    if request.method == 'GET':
        return render(request, 'hosts/group_edit.html', {'group': group})
    elif request.method == 'POST':
        g_name = request.POST.get('g_name')
        g_comment = request.POST.get('g_comment')
        try:
            if g_name != group.name:
                check_name = HostNode.objects.filter(name=g_name)
                if check_name:
                    return render(request, 'hosts/node_create.html', {'error': '组名称已经存在，请重新填写'})
                group.name = g_name
            group.comment = g_comment
            group.save()
            return render(request, 'hosts/group_list.html')
        except Exception as e:
            return render(request, 'hosts/group_edit.html', {'group': group, 'error': '组编辑失败，请检查'})


def group_del(request):
    id = int(request.GET.get('id'))
    try:
        HostGroup.objects.filter(id=id).delete()
        return JsonResponse({'result': True})
    except Exception as e:
        return JsonResponse({'result': False})


