# coding=utf-8

import time

class GetTime(object):

    def get_system_time(self):
        #print (time.time())
        #print (time.localtime())
        new_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) # 格式化时间，按照2019-4-26 17:46:30的格式展示
        print (new_time)

gettime = GetTime()
gettime.get_system_time()