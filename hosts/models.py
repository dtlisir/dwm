from django.db import models
from blueapps.account.models import User

class HostGroup(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='名称')
    created_by = models.CharField(max_length=32, blank=True, verbose_name='创建者')
    date_created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='创建时间')
    comment = models.TextField(blank=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '主机组'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_by': self.created_by,
            'node_count': self.nodes.filter(group=self.id).count(),
            'date_created': self.date_created.strftime("%Y-%m-%d %H:%M:%S"),
            'comment': self.comment,
        }

class HostNode(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='名称')
    url = models.CharField(max_length=128, unique=True, verbose_name='URL')
    ip = models.CharField(max_length=32, blank=True, verbose_name='IP')
    comment = models.TextField(blank=True, verbose_name='备注')
    created_by = models.CharField(max_length=32, blank=True, verbose_name='创建者')
    date_created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='创建时间')
    group = models.ForeignKey(HostGroup, on_delete=models.SET_NULL, related_name='nodes',
                              blank=True, null=True, verbose_name='组名')

    os = models.CharField(max_length=128, blank=True, verbose_name='操作系统')
    os_arch = models.CharField(max_length=16, blank=True, verbose_name='架构')
    cpu_count = models.IntegerField(default=0, blank=True, null=True, verbose_name='CPU核数')
    memory = models.IntegerField(default=0, blank=True, null=True,verbose_name='内存总量')
    active = models.BooleanField(default=False, blank=True, verbose_name='状态')
    c_running = models.IntegerField(default=0, blank=True, null=True,verbose_name='运行数')
    c_paused = models.IntegerField(default=0, blank=True, null=True,verbose_name='暂停数')
    c_stopped = models.IntegerField(default=0, blank=True, null=True,verbose_name='停止数')
    check_time = models.DateTimeField(auto_now=True, blank=True, verbose_name='检测时间')
    d_version = models.CharField(max_length=32, blank=True, verbose_name='Docker版本')
    c_count = models.IntegerField(default=0, blank=True, null=True,verbose_name='容器数')
    i_count = models.IntegerField(default=0, blank=True, null=True,verbose_name='镜像数')

    users = models.ManyToManyField(User, blank=True, related_name='nodes', verbose_name='授权用户')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '主机'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'active': self.active,
            'check_time': self.check_time.strftime("%Y-%m-%d %H:%M:%S"),
            'url': self.url,
            'group': self.group.name if self.group else '',
        }

