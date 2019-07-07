# -*- coding: utf-8 -*-
import time

def timestamp_to_datetime(timestamp):
    time_array = time.localtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", time_array)