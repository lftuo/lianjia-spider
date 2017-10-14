#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-10-12 12:26:20
# @File : ChengjiaoAreaSpider.py
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
            url = "https://gz.lianjia.com/chengjiao/"
            proxies = {"https": "http://114.99.3.254:6890"}
            # user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"
            # user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
            user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0"
            headers = {'User-Agent': user_agent}
            r = requests.get(url, headers=headers, proxies=proxies)
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
        proxies = {"https": "http://114.99.3.254:6890"}
        r = requests.get(url, headers=headers,proxies=proxies)
        soup = BeautifulSoup(r.text,'lxml',from_encoding='utf-8')
        # 爬取分页数据列表
        if soup.find(class_="page-box house-lst-page-box") is not None:
            page_data = soup.find_all("div",class_="page-box house-lst-page-box")[0]['page-data']
            page_url = soup.find_all("div",class_="page-box house-lst-page-box")[0]['page-url']
            title = ""
            detail_url = ""
            deal_date = ""

            if int(json.loads(page_data).get("totalPage")) > 0:
                for i in range(int(json.loads(page_data).get("totalPage"))):
                #print page_url,i+1
                    try:
                        new_url = urlparse.urljoin(url,re.sub(r"{page}",str(i+1),page_url))
                        # 爬取房源信息详情页
                        r = requests.get(new_url, headers=headers,proxies=proxies)
                        soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf-8')
                        # print soup.prettify()
                        if len(soup.find_all(class_="listContent")) > 0:
                            for each in soup.find_all(class_="listContent")[0].find_all("li"):
                                try:
                                    if len(each.find_all("div", class_="info")) == 1 :
                                        title = each.find_all("div", class_="info")[0].find(class_="title").a.string
                                        detail_url = each.find_all("div", class_="info")[0].a['href']
                                    if len(each.find_all("div", class_="address")) == 1:
                                        deal_date = each.find_all("div", class_="address")[0].find(class_="dealDate").string
                                    if len(each.find_all("div", class_="flood")) == 1:
                                        price = each.find_all("div", class_="flood")[0].find(class_="unitPrice").find(class_="number").string
                                    print title,',', price,',',deal_date,',',detail_url
                                    content = (title, price, deal_date, detail_url)
                                    if len(content) == 4:
                                        try:
                                            # 连接sqlite数据库
                                            conn = sqlite3.connect('E:/tuotuo/dbdata/gz_lianjia_link.db')
                                            cur = conn.cursor()
                                            cur.execute(' INSERT INTO gz_lianjia_link_panyu VALUES (?,?,?,?)',content)
                                            conn.commit()
                                            conn.close()
                                        except Exception, e:
                                            print e
                                except Exception,e:
                                    print e

                    except Exception,e:
                        print e

    # 解析经纬度
    def spider_position_info(self, url):
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"
        #headers = {'User-Agent': user_agent}
        proxies = {"https": "117.57.23.128:6890"}
        r = requests.get(url, headers=hds[random.randint(0,len(hds)-1)],proxies=proxies)
        #r = requests.get(url, headers=headers)
        #print r.text
        soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf-8')
        details = soup.find_all(text=re.compile("resblockPosition"))
        if len(details) > 0:
            pattern = re.compile(r"(resblockPosition:')(\d+.\d+)(,)(\d+.\d+)'")
            longitude = re.search(pattern, details[0]).group(2)
            latitude = re.search(pattern, details[0]).group(4)
            return longitude, latitude

    def create_linkdb(self):
        conn = sqlite3.connect('E:/tuotuo/dbdata/gz_lianjia_link.db')
        # 创建sqlite数据库
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS gz_lianjia_link_panyu(house_name VARCHAR(100),price VARCHAR(20),deal_date VARCHAR(20),detail_url VARCHAR(50))')
        conn.close()

    # 更新数据库经纬度信息
    def update_db(self,tablename):

        conn = sqlite3.connect('E:/tuotuo/dbdata/gz_lianjia_link.db')
        # 创建sqlite数据库
        cur = conn.cursor()
        cur.execute(' SELECT * FROM (%s)'%tablename)
        res = cur.fetchall()
        try:
            for line in res:
                try:
                    if line[6] == 0:
                        url = line[3]
                        location = spider_area.spider_position_info(url)
                        if len(location) == 2:
                            longitude = location[0]
                            latitude = location[1]
                            print line[0],url,longitude,latitude
                            # 刷新数据库经纬度信息
                            cur.execute('UPDATE gz_lianjia_link_panyu SET longitude = ?,latitude = ?,flag = 1 WHERE flag == 0 AND detail_url = ?',(longitude,latitude,url))
                            conn.commit()
                except Exception,e:
                    print e.message
        except Exception,e:
            print e.message
        finally:
            conn.close()



if __name__ == '__main__':
    '''
    URL:
    https://gz.lianjia.com/chengjiao/tianhe/
    https://gz.lianjia.com/chengjiao/yuexiu/
    https://gz.lianjia.com/chengjiao/liwan/
    https://gz.lianjia.com/chengjiao/haizhu/
    https://gz.lianjia.com/chengjiao/panyu/
    https://gz.lianjia.com/chengjiao/baiyun/
    https://gz.lianjia.com/chengjiao/huangpugz/
    https://gz.lianjia.com/chengjiao/conghua/
    https://gz.lianjia.com/chengjiao/zengcheng/
    https://gz.lianjia.com/chengjiao/huadou/
    https://gz.lianjia.com/chengjiao/nansha/
    '''
    spider_area = spider_area()
    # 创建数据库
    #spider_area.create_linkdb()
    # 爬取大区链接
    #spider_area.spider_url_area()
    # 爬取住房链接
    #spider_area.spider_list_url('https://gz.lianjia.com/chengjiao/baiyun/')
    # 爬取经纬度信息
    spider_area.update_db('gz_lianjia_link_panyu')
