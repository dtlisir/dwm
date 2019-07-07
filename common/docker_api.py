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


def get_container_info(url):
    try:
        client = docker.DockerClient(base_url=url)
        data = client.containers.list(all=True)
        resp = {'result': True, 'data': data}
        client.close()
    except Exception as e:
        resp = {'result': False, 'message': str(e)}
    return resp






