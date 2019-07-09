# -*- coding: utf-8 -*-

import docker

def get_docker_info(url):
    try:
        client = docker.DockerClient(base_url=url)
        data = client.info()
        resp = {'result': True, 'data': data}
        client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp


def get_containers(url):
    try:
        client = docker.DockerClient(base_url=url)
        data = client.containers.list(all=True)
        resp = {'result': True, 'data': data}
        client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp


def run_container(url, image, **kwargs):
    try:
        client = docker.DockerClient(base_url=url)
        data = client.containers.run(image, detach=True, **kwargs)
        resp = {'result': True, 'data': data}
        client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp



def get_images(url):
    try:
        client = docker.DockerClient(base_url=url)
        data = client.images.list()
        resp = {'result': True, 'data': data}
        client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp


def get_volumes(url):
    try:
        client = docker.DockerClient(base_url=url)
        data = client.volumes.list()
        resp = {'result': True, 'data': data}
        client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp


def get_networks(url):
    try:
        client = docker.DockerClient(base_url=url)
        data = client.networks.list()
        resp = {'result': True, 'data': data}
        client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp







