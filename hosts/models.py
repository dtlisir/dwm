from django.db import models

class HostGroup(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='名称')
    created_by = models.CharField(max_length=32, blank=True, verbose_name='创建者')
    date_created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='创建时间')
    comment = models.TextField(blank=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '节点分组'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_by': self.created_by,
            'node_count': self.host_nodes.filter(group=self.id).count(),
            'date_created': self.date_created.strftime("%Y-%m-%d %H:%M:%S"),
            'comment': self.comment,
        }

class HostNode(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='名称')
    is_active = models.BooleanField(default=False, blank=True, verbose_name='状态')
    check_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='检测时间')
    node_url = models.CharField(max_length=128, unique=True, verbose_name='节点URL')
    ip = models.CharField(max_length=32, blank=True, verbose_name='IP')
    group = models.ForeignKey(HostGroup, on_delete=models.SET_NULL, related_name='host_nodes',
                              blank=True, null=True, verbose_name='主机分组')
    admin_users = models.TextField(blank=True, verbose_name='授权用户')
    hostname = models.CharField(max_length=128, blank=True, verbose_name='主机名')
    server_version = models.CharField(max_length=32, blank=True, verbose_name='Docker版本')
    container_total = models.IntegerField(default=0, blank=True, verbose_name='容器总数')
    container_running = models.IntegerField(default=0, blank=True, verbose_name='容器运行数')
    container_paused = models.IntegerField(default=0, blank=True, verbose_name='容器暂停数')
    container_stopped = models.IntegerField(default=0, blank=True,verbose_name='容器停止数')
    images = models.IntegerField(default=0, blank=True, verbose_name='镜像总数')
    cpu_count = models.IntegerField(default=0, blank=True, verbose_name='CPU核心')
    memory = models.CharField(max_length=128, blank=True, verbose_name='内存总量')
    os = models.CharField(max_length=128, blank=True, verbose_name='操作系统')
    os_arch = models.CharField(max_length=16, blank=True, verbose_name='系统架构')
    created_by = models.CharField(max_length=32, blank=True, verbose_name='创建者')
    date_created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='创建时间')
    comment = models.TextField(blank=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '宿主节点'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'is_active': self.is_active,
            'check_time': self.check_time.strftime("%Y-%m-%d %H:%M:%S"),
            'node_url': self.node_url,
            'group': self.group.name if self.group else '',
        }

