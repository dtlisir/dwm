# -*- coding: utf-8 -*-

import docker

def get_docker_info(url):
    try:
        client = docker.DockerClient(base_url=url)
        try:
            data = client.info()
            resp = {'result': True, 'data': data}
        finally:
            client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp


def get_containers(url):
    try:
        client = docker.DockerClient(base_url=url)
        try:
            data = client.containers.list(all=True)
            resp = {'result': True, 'data': data}
        finally:
            client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp


def get_container_detail(url, id):
    try:
        client = docker.DockerClient(base_url=url)
        try:
            data = client.containers.get(id)
            resp = {'result': True, 'data': data}
        finally:
            client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp


def start_container(url, id):
    try:
        client = docker.DockerClient(base_url=url)
        try:
            container = client.containers.get(id)
            container.start()
            resp = {'result': True}
        finally:
            client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp


def stop_container(url, id):
    try:
        client = docker.DockerClient(base_url=url)
        try:
            container = client.containers.get(id)
            container.stop()
            resp = {'result': True}
        finally:
            client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp


def restart_container(url, id):
    try:
        client = docker.DockerClient(base_url=url)
        try:
            container = client.containers.get(id)
            container.restart()
            resp = {'result': True}
        finally:
            client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp


def pause_container(url, id):
    try:
        client = docker.DockerClient(base_url=url)
        try:
            container = client.containers.get(id)
            container.pause()
            resp = {'result': True}
        finally:
            client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp


def run_container(url, image, **kwargs):
    try:
        client = docker.DockerClient(base_url=url)
        try:
            data = client.containers.run(image, detach=True, **kwargs)
            resp = {'result': True, 'data': data}
        finally:
            client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp


def get_images(url):
    try:
        client = docker.DockerClient(base_url=url)
        try:
            data = client.images.list()
            resp = {'result': True, 'data': data}
        finally:
            client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp


def get_volumes(url):
    try:
        client = docker.DockerClient(base_url=url)
        try:
            data = client.volumes.list()
            resp = {'result': True, 'data': data}
        finally:
            client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp


def get_networks(url):
    try:
        client = docker.DockerClient(base_url=url)
        try:
            data = client.networks.list()
            resp = {'result': True, 'data': data}
        finally:
            client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp







