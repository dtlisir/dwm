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
        verbose_name = '主机分组'

    @classmethod
    def initial(cls):
        host_group = cls(name='默认组', comment='默认的宿主机分组')
        host_group.save()


class HostNode(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='名称')
    group = models.ForeignKey(HostGroup, on_delete=models.CASCADE, related_name='host_nodes', verbose_name='主机分组')
    admin_users = models.TextField(blank=True, verbose_name='授权用户')
    ip = models.CharField(max_length=32, blank=True, verbose_name='IP')
    conn_url = models.CharField(max_length=128, unique=True, verbose_name='节点URL')
    hostname = models.CharField(max_length=128, blank=True, verbose_name='主机名')
    is_active = models.BooleanField(default=False, blank=True, verbose_name='状态')
    server_version = models.CharField(max_length=32, blank=True, verbose_name='Docker版本')
    container_total = models.IntegerField(default=0, verbose_name='容器总数')
    container_running = models.IntegerField(default=0, verbose_name='容器运行数')
    container_paused = models.IntegerField(default=0, verbose_name='容器暂停数')
    container_stopped = models.IntegerField(default=0, verbose_name='容器停止数')
    images = models.IntegerField(default=0, verbose_name='镜像总数')
    cpu_count = models.IntegerField(default=0, blank=True, verbose_name='CPU核心')
    system_time = models.DateTimeField(blank=True, verbose_name='创建时间')
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



