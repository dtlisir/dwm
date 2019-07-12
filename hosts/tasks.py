# -*- coding: utf-8 -*-

import time
from django.utils import timezone
from celery.schedules import crontab
from celery.task import periodic_task
from .models import HostNode
from syslogs.models import Log
from common.docker_api import get_docker_info


@periodic_task(run_every=crontab(minute='*/30', hour='*', day_of_week="*"))
def check_node_data_periodic():
    try:
        nodes = HostNode.objects.all()
        for node in nodes:
            resp = get_docker_info(node.url)
            if resp['result']:
                data = resp['data']
                node.os = data['OperatingSystem'],
                node.os_arch = data['Architecture'],
                node.cpu_count = data['NCPU'],
                node.memory = data['MemTotal'],
                node.active = True,
                node.check_time = timezone.now(),
                node.c_running = data['ContainersRunning'],
                node.c_paused = data['ContainersPaused'],
                node.c_stopped = data['ContainersStopped'],
                node.d_version = data['ServerVersion'],
                node.c_count = data['Containers'],
                node.i_count = data['Images']
                node.save()
            else:
                node.active = False
                node.save()
            time.sleep(1)
        Log.objects.create(user='system', type='HOST', action='CHECK', content='主机巡检成功')
    except Exception as e:
        Log.objects.create(user='system', type='HOST', action='CHECK', content='主机巡检失败')

