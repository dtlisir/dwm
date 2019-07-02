#!/bin/bash

# 关闭防火墙
systemctl stop firewalld.service
systemctl disable firewalld.service

#禁用selinux
sed -i "s/SELINUX=enforcing/SELINUX=disabled/" /etc/selinux/config
setenforce 0

yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum makecache fast
yum -y install docker-ce
#docker镜像加速
mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://2x42e901.mirror.aliyuncs.com"]
}
EOF
#开启docker远程访问
get_lan_ip () {
   /usr/sbin/ip addr | \
       awk -F'[ /]+' '/inet/{
               split($3, N, ".")
               if ($3 ~ /^192.168/) {
                   print $3
               }
               if (($3 ~ /^172/) && (N[2] >= 16) && (N[2] <= 31)) {
                   print $3
               }
               if ($3 ~ /^10\./) {
                   print $3
               }
          }'

   return $?
}
lan_ip=$(get_lan_ip | head -1)
old="-H fd://"
new="-H tcp://${lan_ip}:2375 -H fd://"
sed -i "s#${old}#${new}#" /lib/systemd/system/docker.service

systemctl daemon-reload
systemctl enable docker
systemctl start docker