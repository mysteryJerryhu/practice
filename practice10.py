# coding:utf-8
"""
 time模块中时间表现的格式主要有三种：

　　a、timestamp 时间戳，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量

　　b、struct_time 时间元组，共有九个元素组。

　　c、format time 格式化时间，已格式化的结构使时间更具可读性。包括自定义格式和固定格式。

转换图：

            .strptime()--->                         .mktime()--->
Format time-----------------------struct_time----------------------------timestamp
            <---.strftime()                   <---.localtime()/.gmtime()


               .asctime()                                       .ctime()
struct_time--------------------> %a %b %d %H:%M:%S %Y 串 <--------------------timestamp

"""
from datetime import *
import time

print('datetime.max:', datetime.max)

print('datetime.min:', datetime.min)          # datetime所能表示的最小值与最大值

print('datetime.resolution:', datetime.resolution)      # datetime最小单位

print('today:', datetime.today())       # 返回一个表示当前本地时间的datetime对象

print('now:', datetime.now())           # 返回一个表示当前本地时间的datetime对象，如果提供了参数，则获取参数所指时区的本地时间

print('utc now:', datetime.utcnow())    # 返回一个当前utc时间的datetime对象

print('from timestamp:', datetime.fromtimestamp(time.time()))  # 根据时间戮创建一个datetime对象，参数指定时区信息；

print('utc from timestamp:', datetime.utcfromtimestamp(time.time()))    # 根据时间戮创建一个datetime对象


