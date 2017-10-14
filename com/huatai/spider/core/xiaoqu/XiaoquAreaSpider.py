#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-10-12 13:29:06
# @File : XiaoquAreaSpider.py
# @Software : PyCharm
import json
import random
import re
import sqlite3

import bs4
import requests
from bs4 import BeautifulSoup
import urlparse

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

class spider_area(object):
    def spider_url_area(self):
        try:
            url = "https://gz.lianjia.com/xiaoqu/rs/"
            # proxies = {"https": "http://115.216.230.209:3936"}
            # r = requests.get(url, headers=hds[random.randint(0,len(hds)-1)], proxies=proxies)
            r = requests.get(url, headers=hds[random.randint(0, len(hds) - 1)])
            #print r.text
        except Exception, e:
            print e.message
        if r.text is not None:
            soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf-8')
            for child in soup.find(class_="position").children:
                if type(child.find("div")) == bs4.element.Tag:
                    for link in child.find("div").find_all("a"):
                        # 获取大区域链接
                        new_url = urlparse.urljoin(url, link['href'])
                        print new_url


    def spider_list_url(self,url):
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0"
        headers = {'User-Agent': user_agent}
        # proxies = {"https": "http://117.95.31.73:2671"}
        # r = requests.get(url, headers=hds[random.randint(0,len(hds)-1)],proxies=proxies)
        r = requests.get(url, headers=hds[random.randint(0, len(hds) - 1)])
        soup = BeautifulSoup(r.text,'lxml',from_encoding='utf-8')
        # 爬取分页数据列表
        if soup.find(class_="page-box house-lst-page-box") is not None:
            page_data = soup.find_all("div",class_="page-box house-lst-page-box")[0]['page-data']
            page_url = soup.find_all("div",class_="page-box house-lst-page-box")[0]['page-url']

            if int(json.loads(page_data).get("totalPage")) > 0:
                for i in range(int(json.loads(page_data).get("totalPage"))):
                    try:
                        new_url = urlparse.urljoin(url,re.sub(r"{page}",str(i+1),page_url))
                        # 爬取房源信息详情页
                        # r = requests.get(new_url, headers=headers,proxies=proxies)
                        r = requests.get(new_url,headers=hds[random.randint(0, len(hds) - 1)])
                        soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf-8')
                        # print soup.prettify()
                        if len(soup.find_all(class_="listContent")) > 0:
                            for each in soup.find_all(class_="listContent")[0].find_all("li"):
                                try:
                                    if len(each.find_all("div", class_="info")) == 1 :
                                        title = each.find_all("div", class_="info")[0].find(class_="title").a.string
                                        detail_url = each.find_all("div", class_="info")[0].a['href']
                                    if each.find_all(class_="tagList")[0].span is not None:
                                        tag_list = each.find(class_="tagList").span.string
                                    else:
                                        tag_list = ""
                                    if len(each.find_all("div", class_="xiaoquListItemPrice")) == 1:
                                        price = each.find_all("div", class_="xiaoquListItemPrice")[0].find(class_="totalPrice").span.string
                                    print title,price,detail_url,tag_list

                                    # 插入空值依次为经度、纬度，0位是否爬取经纬度标识
                                    content = (title,price,'','',detail_url,tag_list,0)
                                    if len(content) == 7:
                                        try:
                                            conn = sqlite3.connect('E:/tuotuo/dbdata/gz_lianjia_xiaoqu.db')
                                        # 创建sqlite数据库
                                            cur = conn.cursor()
                                            cur.execute(' INSERT INTO gz_lianjia_xiaoqu_tianhe VALUES(?,?,?,?,?,?,?)',content)
                                            conn.commit()
                                            conn.close()
                                        except Exception, e:
                                            print e
                                except Exception,e:
                                    print e

                    except Exception,e:
                        print e

    def create_linkdb(self):
        conn = sqlite3.connect('E:/tuotuo/dbdata/gz_lianjia_xiaoqu.db')
        # 创建sqlite数据库
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS gz_lianjia_xiaoqu_tianhe('
                    'title VARCHAR(100),'
                    'price VARCHAR(20),'
                    'longitude VARCHAR(50),'
                    'latitude VARCHAR(50),'
                    'detail_url VARCHAR(50),'
                    'tag_list VARCHAR(100),flag integer)')
        conn.close()

if __name__ == '__main__':
    '''
    URL:
    https://gz.lianjia.com/xiaoqu/tianhe/
    https://gz.lianjia.com/xiaoqu/yuexiu/
    https://gz.lianjia.com/xiaoqu/liwan/
    https://gz.lianjia.com/xiaoqu/haizhu/
    https://gz.lianjia.com/xiaoqu/panyu/
    https://gz.lianjia.com/xiaoqu/baiyun/
    https://gz.lianjia.com/xiaoqu/huangpugz/
    https://gz.lianjia.com/xiaoqu/conghua/
    https://gz.lianjia.com/xiaoqu/zengcheng/
    https://gz.lianjia.com/xiaoqu/huadou/
    https://gz.lianjia.com/xiaoqu/nansha/
    '''
    spider_area = spider_area()
    # 爬取大区链接
    # spider_area.spider_url_area()
    # 创建数据库
    spider_area.create_linkdb()
    # 爬取住房链接
    spider_area.spider_list_url('https://gz.lianjia.com/xiaoqu/tianhe/')
