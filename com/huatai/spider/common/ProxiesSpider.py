#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-10-14 12:46:24
# @File : ProxiesSpider.py
# @Software : PyCharm
# 爬取国内http代理网站http://www.xicidaili.com/wt/
import random
import sqlite3

import requests
from bs4 import BeautifulSoup

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

class proxies_spider(object):
    '''
    获取代理网站表格
    :param page_nums 代理网站http://www.xicidaili.com/wt/总页数
    '''
    def spider_list(self,page_nums):
        parent_url = "http://www.xicidaili.com/wt/"
        for i in range(page_nums):
            child_url = parent_url+'%s'%(i+1)
            try:
                # 解析子网页url
                r = requests.get(child_url, headers=hds[random.randint(0, len(hds) - 1)])
                soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf-8')
                for line in soup.find_all("tr"):
                    try:
                        # 解析每一行数据
                        if len(line.find_all("td")) == 10:
                            tds = line.find_all("td")
                            # 获取"IP地址"
                            ip_addr = tds[1].string
                            # 获取"端口"
                            port = tds[2].string
                            # 获取"服务器地址"
                            if tds[3].find("a") is not None:
                                service_address = tds[3].a.string
                            else:
                                service_address = " "
                            # 获取"速度"百分数
                            speed_percent = tds[6].find(class_="bar").find("div")['style'].split(":")[1].split("%")[0]
                            # 获取"连接时间"百分数
                            connect_percent = tds[7].find(class_="bar").find("div")['style'].split(":")[1].split("%")[0]
                            # 获取"存活时间"
                            survive_time = tds[8].string
                            # 获取"验证时间"
                            identify_time = tds[9].string
                            print ip_addr,port,service_address,speed_percent,connect_percent,survive_time,identify_time
                            content = (ip_addr,port,service_address,speed_percent,connect_percent,survive_time,identify_time)
                            if len(content) == 7:
                                try:
                                    conn = sqlite3.connect('E:/tuotuo/dbdata/proxies_ips.db')
                                    # 创建sqlite数据库
                                    cur = conn.cursor()
                                    cur.execute(' INSERT INTO proxies_ips VALUES(?,?,?,?,?,?,?)', content)
                                    conn.commit()
                                    conn.close()
                                except Exception, e:
                                    print e
                    except Exception,e:
                        print e.message
            except Exception,e:
                print e.message
    '''
    创建存放代理ip的数据库
    '''
    def create_table(self):
        # 创建sqlite数据库连接，如果数据库不存在，则创建
        conn = sqlite3.connect('E:/tuotuo/dbdata/proxies_ips.db')
        cur = conn.cursor()
        cur.execute('DROP TABLE proxies_ips')
        cur.execute('CREATE TABLE IF NOT EXISTS proxies_ips('
                    'ip_addr VARCHAR(20),'
                    'port VARCHAR(10),'
                    'service_address VARCHAR(50),'
                    'speed_percent integer,'
                    'connect_percent integer(50),'
                    'survive_time VARCHAR(100),'
                    'identify_time VARCHAR(50))')
        conn.close()
    '''
    爬取链家网测试
    '''
    def spider_lianjia(self):
        # 创建sqlite数据库连接
        conn = sqlite3.connect('E:/tuotuo/dbdata/proxies_ips.db')
        cur = conn.cursor()
        # 查询ip库
        cur.execute("SELECT ip_addr,port FROM proxies_ips WHERE speed_percent >= 95 AND connect_percent >= 95 ORDER BY identify_time DESC;")
        res = cur.fetchall()
        for line in res:
            ip = line[0]
            port = line[1]
            try:
                proxies = {"https":"%s:%s"%(ip,port)}
                url = "https://gz.lianjia.com/xiaoqu/2110343238599253/"
                requests.get(url, headers=hds[random.randint(0, len(hds) - 1)], proxies=proxies,timeout=3)
                print ip+':%s'%port,
            except Exception,e:
                print e.message

if __name__ == '__main__':
    spider = proxies_spider()
    # 创建ip数据库
    #spider.create_table()
    # 爬取代理网站信息
    #spider.spider_list(2)
    # 测试是否能够爬取链家
    spider.spider_lianjia()
