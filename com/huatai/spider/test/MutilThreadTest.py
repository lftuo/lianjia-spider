#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-10-12 08:46:55
# @File : MutilThreadTest.py
# @Software : PyCharm
import threading
import time
import sqlite3

exitFlag = 0

class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "Starting " + self.name
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        for i in range(10):
            data = "'1','qiye','20'"
            cur.execute(' INSERT INTO person VALUES (%s)' % data)
        counter -= 1


conn = sqlite3.connect('E:/tuotuo/dbdata/test.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS person (id VARCHAR(20),name VARCHAR(20),age VARCHAR(20))')

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

print "Exiting Main Thread"