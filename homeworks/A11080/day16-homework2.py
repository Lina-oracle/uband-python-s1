#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Jiaguwen

import time

ticks = time.time()
print '当前时间戳为： ', ticks

localtime = time.localtime(time.time())
print '当地时间为：', localtime

localtime = time.asctime( time.localtime(time.time()) )
print '当地时间为：', localtime