# -*- coding: utf-8 -*-
import time
import datetime


def timestamp_to_datetime(timestamp):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))


def http_to_timestamp(time_str):
    return time.mktime(time.strptime(time_str, "%a, %d %b %Y %H:%M:%S GMT"))


def iso8601_to_timestamp(time_str):
    return time.mktime(time.strptime(time_str, "%Y-%m-%dT%H:%M:%S"))


def handle_size(size):
    if not size:
        return ''
    return '%dMB' % (int(size)/1024/1024)


def handle_time(time_str):
    utc_time = datetime.datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S")
    local_time = utc_time + datetime.timedelta(hours=8)
    return datetime.datetime.strftime(local_time, "%Y-%m-%d %H:%M:%S")
