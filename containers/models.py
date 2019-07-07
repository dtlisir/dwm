from django.db import models
# from images.models import Image
# from volumes.models import Volume
# from networks.models import Network
# from hosts.models import HostNode
#
#
# class Container(models.Model):
#     c_id = models.CharField(max_length=128, unique=True, verbose_name='容器ID')
#     c_name = models.CharField(max_length=128, blank=True, verbose_name='名称')
#     ip = models.CharField(max_length=32, blank=True, verbose_name='IP')
#     status = models.BooleanField(default=False, blank=True, verbose_name='状态')
#     created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='创建时间')
#     s_time = models.DateTimeField(blank=True, verbose_name='启动时间')
#     image = models.ForeignKey(Image, on_delete=models.CASCADE, verbose_name='镜像')
#     p_port = models.TextField(blank=True, verbose_name='映射端口')
#     command = models.TextField(blank=True, verbose_name='命令')
#     r_policy = models.CharField(max_length=64, blank=True, verbose_name='重启策略')
#     volumes = models.ForeignKey(Volume, on_delete=models.CASCADE, verbose_name='挂载卷')
#     networks = models.ForeignKey(Network, on_delete=models.CASCADE, verbose_name='网络')
#     node = models.ForeignKey(HostNode, on_delete=models.CASCADE, verbose_name='节点')
#
#     def __str__(self):
#         return self.c_name
#
#     class Meta:
#         verbose_name = '容器'

