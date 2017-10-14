#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-10-12 16:25:10
# @File : SpiderPositionInfo.py
# @Software : PyCharm
import random
import re
import sqlite3

import requests
from bs4 import BeautifulSoup
import time


hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
    {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
    {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]


class spider_position_info(object):
    # 解析经纬度
    def spider_position_info(self, url):
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"
        headers = {'User-Agent': user_agent}
        proxies = {"https": "125.67.70.46:2132"}
        r = requests.get(url, headers=hds[random.randint(0,len(hds)-1)], proxies=proxies)
        #r = requests.get(url, headers=headers)
        # print r.text
        soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf-8')
        details = soup.find_all(text=re.compile("resblockPosition"))
        if len(details) > 0:
            pattern = re.compile(r"(resblockPosition:')(\d+.\d+)(,)(\d+.\d+)'")
            longitude = re.search(pattern, details[0]).group(2)
            latitude = re.search(pattern, details[0]).group(4)
            return longitude, latitude
            # 更新数据库经纬度信息

    def update_db(self, tablename):
        conn = sqlite3.connect('E:/tuotuo/dbdata/gz_lianjia_link.db')
        # 创建sqlite数据库
        cur = conn.cursor()
        cur.execute(' SELECT * FROM (%s)' % tablename)
        res = cur.fetchall()
        try:
            i = 0
            for line in res:
                try:
                    if line[6] == 0:
                        url = line[3]
                        location = position.spider_position_info(url)
                        if len(location) == 2:
                            longitude = location[0]
                            latitude = location[1]
                            print line[0], url, longitude, latitude
                            # 刷新数据库经纬度信息
                            cur.execute(
                                'UPDATE gz_lianjia_link_panyu SET longitude = ?,latitude = ?,flag = 1 WHERE flag == 0 AND detail_url = ?',
                                (longitude, latitude, url))
                            conn.commit()
                except Exception, e:
                    print e.message
        except Exception, e:
            print e.message
        finally:
            conn.close()
if __name__ == '__main__':
    position = spider_position_info()
    position.update_db('gz_lianjia_link_panyu')