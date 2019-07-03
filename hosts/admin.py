from django.contrib import admin
from .models import HostGroup, HostNode

admin.site.register(HostGroup)
admin.site.register(HostNode)


