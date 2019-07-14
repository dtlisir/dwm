from django.shortcuts import render
from django.http import JsonResponse
from hosts.models import CurrNode
from common.docker_api import get_containers, get_container_detail, get_images
from common.docker_api import start_container, stop_container, restart_container, pause_container
from common.utils import handle_time
from syslogs.models import Log


def container_list(request):
    curr_node = CurrNode.objects.all()
    if not curr_node:
        return render(request, 'home/select_node.html')
    return render(request, 'containers/container_list.html', {'node': curr_node[0]})


def get_container_list(request):
    try:
        resp_data = []
        url = request.POST.get('node_url')
        resp = get_containers(url)
        if resp['result']:
            for data in resp['data']:
                c_data = {
                    'c_id': data.id,
                    'name': data.name,
                    'image': data.image.attrs['RepoTags'][0] if data.image.attrs['RepoTags'] else '',
                    'created': handle_time(data.attrs['Created'][:-11]),
                    'status': data.status,
                }
                resp_data.append(c_data)
        return JsonResponse({'data': resp_data})
    except Exception as e:
        return JsonResponse({'data': []})


def container_create(request):
    images = []
    curr_node = CurrNode.objects.all()
    if not curr_node:
        return render(request, 'home/select_node.html')
    node_url = curr_node[0].node_url
    resp = get_images(node_url)
    if resp['result']:
        resp_data = resp['data']
        for r_data in resp_data:
            images.append(r_data.tags[0])
    return render(request, 'containers/container_create.html', {'images': images})


def container_detail(request, id):
    curr_node = CurrNode.objects.all()
    if not curr_node:
        return render(request, 'home/select_node.html')
    node_name = curr_node[0].node_name
    node_url = curr_node[0].node_url
    data = {}
    try:
        resp = get_container_detail(node_url, id)
        if resp['result']:
            resp_data = resp['data']
            data = {
                'id': resp_data.id,
                'name': resp_data.name,
                'status': resp_data.status,
                'image_id': resp_data.attrs['Image'],
                'image_name': resp_data.image.tags[0] if resp_data.image.tags else '',
                'created': handle_time(resp_data.attrs['Created'][:-11]),
                'node_name': node_name,
                'node_url': node_url,
            }
        return render(request, 'containers/container_detail.html', {'data': data})
    except Exception as e:
        return render(request, 'containers/container_detail.html', {'data': {}})


def post_container_start(request):
    node_url = request.POST.get('node_url')
    c_id = request.POST.get('c_id')
    c_name = request.POST.get('c_name')
    user = request.user.username
    resp = start_container(node_url, c_id)
    if resp['result']:
        Log.objects.create(
            user=user,
            type='CONTAINER',
            action='START',
            state=True,
            content='容器[%s]启动成功' % (c_name)
        )
        return JsonResponse({'result': True, 'message': '容器启动成功'})
    else:
        Log.objects.create(
            user=user,
            type='CONTAINER',
            action='START',
            state=False,
            content='容器[%s]启动失败，原因：%s' % (c_name, resp['message'])
        )
        return JsonResponse({'result': False, 'message': '容器启动失败，请查看操作日志'})


def post_container_stop(request):
    node_url = request.POST.get('node_url')
    c_id = request.POST.get('c_id')
    c_name = request.POST.get('c_name')
    user = request.user.username
    resp = stop_container(node_url, c_id)
    if resp['result']:
        Log.objects.create(
            user=user,
            type='CONTAINER',
            action='STOP',
            state=True,
            content='容器[%s]停止成功' % (c_name)
        )
        return JsonResponse({'result': True, 'message': '容器停止成功'})
    else:
        Log.objects.create(
            user=user,
            type='CONTAINER',
            action='STOP',
            state=False,
            content='容器[%s]停止失败，原因：%s' % (c_name, resp['message'])
        )
        return JsonResponse({'result': False, 'message': '容器停止失败，请查看操作日志'})


def post_container_restart(request):
    node_url = request.POST.get('node_url')
    c_id = request.POST.get('c_id')
    c_name = request.POST.get('c_name')
    user = request.user.username
    resp = restart_container(node_url, c_id)
    if resp['result']:
        Log.objects.create(
            user=user,
            type='CONTAINER',
            action='RESTART',
            state=True,
            content='容器[%s]重启成功' % (c_name)
        )
        return JsonResponse({'result': True, 'message': '容器重启成功'})
    else:
        Log.objects.create(
            user=user,
            type='CONTAINER',
            action='RESTART',
            state=False,
            content='容器[%s]重启失败，原因：%s' % (c_name, resp['message'])
        )
        return JsonResponse({'result': False, 'message': '容器重启失败，请查看操作日志'})


def post_container_pause(request):
    node_url = request.POST.get('node_url')
    c_id = request.POST.get('c_id')
    c_name = request.POST.get('c_name')
    user = request.user.username
    resp = pause_container(node_url, c_id)
    if resp['result']:
        Log.objects.create(
            user=user,
            type='CONTAINER',
            action='PAUSE',
            state=True,
            content='容器[%s]暂停成功' % (c_name)
        )
        return JsonResponse({'result': True, 'message': '容器暂停成功'})
    else:
        Log.objects.create(
            user=user,
            type='CONTAINER',
            action='PAUSE',
            state=False,
            content='容器[%s]暂停失败，原因：%s' % (c_name, resp['message'])
        )
        return JsonResponse({'result': False, 'message': '容器暂停失败，请查看操作日志'})
