from django.db import models

class Log(models.Model):
    user = models.CharField(max_length=64, blank=True, verbose_name='用户')
    type = models.CharField(max_length=64, blank=True, verbose_name='分类')
    action = models.CharField(max_length=64, blank=True, verbose_name='动作')
    state = models.BooleanField(default=False, blank=True, verbose_name='状态')
    content = models.CharField(max_length=256, blank=True, verbose_name='内容')
    time_ops = models.DateTimeField(auto_now=True, blank=True, verbose_name='时间')

    class Meta:
        verbose_name = '系统日志'

    def to_dict(self):
        return {
            'user': self.user,
            'type': self.type,
            'action': self.action,
            'state': self.state,
            'content': self.content,
            'time_ops': self.time_ops.strftime("%Y-%m-%d %H:%M:%S"),
        }
