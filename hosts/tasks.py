# -*- coding: utf-8 -*-

import time
from django.utils import timezone
from celery.schedules import crontab
from celery.task import periodic_task
from .models import HostNode
from syslogs.models import Log
from common.docker_api import get_docker_info


@periodic_task(run_every=crontab(minute='*/1', hour='*', day_of_week="*"))
def check_node_data_periodic():
    try:
        nodes = HostNode.objects.all()
        for node in nodes:
            resp = get_docker_info(node.url)
            if resp['result']:
                data = resp['data']
                HostNode.objects.filter(id=node.id).update(
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
            else:
                HostNode.objects.filter(id=node.id).update(active=False)
            time.sleep(1)
    except Exception as e:
        content = '主机巡检失败，原因：%s' % (str(e))
        Log.objects.create(
            user='system',
            type='HOST',
            action='CHECK',
            state=False,
            content=content
        )

