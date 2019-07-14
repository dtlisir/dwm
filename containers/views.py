from django.shortcuts import render
from django.http import JsonResponse
from hosts.models import CurrNode
from common.docker_api import get_containers, get_container_detail
from common.utils import handle_time


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

    return render(request, 'containers/container_create.html')


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
                'image_id': resp_data.image.attrs['Id'],
                'image_name': resp_data.image.attrs['RepoTags'][0] if resp_data.image.attrs['RepoTags'] else '',
                'created': handle_time(resp_data.attrs['Created'][:-11]),
                'node_name': node_name,
                'node_url': node_url,
            }
        return render(request, 'containers/container_detail.html', {'data': data})
    except Exception as e:
        return render(request, 'containers/container_detail.html', {'data': {}})
