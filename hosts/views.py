import logging
from django.shortcuts import render
from django.http import JsonResponse
from .models import HostGroup, HostNode

logger = logging.getLogger('app')

def node_list(request):
    return render(request, 'hosts/node_list.html')

def node_create(request):
    if request.method == 'GET':
        return render(request, 'hosts/node_create.html')
    elif request.method == 'POST':
        node_name = request.POST.get('node_name')
        node_url = request.POST.get('node_url')
        node_ip = request.POST.get('node_ip')
        node_comment = request.POST.get('node_comment')
        user = request.user.username
        try:
            HostNode.objects.create(
                name=node_name,
                node_url=node_url,
                ip=node_ip,
                created_by=user,
                comment=node_comment)
            return render(request, 'hosts/node_list.html')
        except Exception as e:
            return render(request, 'hosts/node_create.html', {'error': str(e)})

def get_node_list(request):
    nodes = HostNode.objects.all()
    data = []
    if nodes:
        data = [node.to_dict() for node in nodes]
    return JsonResponse({'data': data})

def node_del(request):
    id = int(request.GET.get('id'))
    try:
        HostGroup.objects.filter(id=id).delete()
        return JsonResponse({'result': True})
    except Exception as e:
        return JsonResponse({'result': False})

def node_edit(request, pk):
    group = HostGroup.objects.get(id=pk)
    if request.method == 'GET':
        return render(request, 'hosts/group_edit.html', {'group': group})
    elif request.method == 'POST':
        g_name = request.POST.get('g_name')
        g_comment = request.POST.get('g_comment')
        user = request.user.username
        try:
            group.name = g_name
            group.created_by = user
            group.comment = g_comment
            group.save()
            return render(request, 'hosts/group_list.html')
        except Exception as e:
            return render(request, 'hosts/group_edit.html', {'group': group, 'info': '组编辑失败，请重新填写'})

def node_detail(request, pk):
    return render(request, 'hosts/node_detail.html')

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
            HostGroup.objects.create(name=g_name, created_by=user, comment=g_comment)
            return render(request, 'hosts/group_list.html')
        except Exception as e:
            return render(request, 'hosts/group_create.html', {'info': '组创建失败，请重新填写'})

def group_edit(request, pk):
    group = HostGroup.objects.get(id=pk)
    if request.method == 'GET':
        return render(request, 'hosts/group_edit.html', {'group': group})
    elif request.method == 'POST':
        g_name = request.POST.get('g_name')
        g_comment = request.POST.get('g_comment')
        user = request.user.username
        try:
            group.name = g_name
            group.created_by = user
            group.comment = g_comment
            group.save()
            return render(request, 'hosts/group_list.html')
        except Exception as e:
            return render(request, 'hosts/group_edit.html', {'group': group, 'info': '组编辑失败，请重新填写'})

def group_del(request):
    id = int(request.GET.get('id'))
    try:
        HostGroup.objects.filter(id=id).delete()
        return JsonResponse({'result': True})
    except Exception as e:
        return JsonResponse({'result': False})


