#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-10-10 15:50:22
# @File : ChengjiaoListSpider.py
# @Software : PyCharm
# 广州成交表单爬取
import bs4
import requests
from bs4 import BeautifulSoup
import re
import urlparse
import json
import csv
import sqlite3
import time

class spider_chengjiao(object):

    def spider_url(self):

        spider = spider_chengjiao()
        spider.create_linkdb()
        try:
            url = "https://gz.lianjia.com/chengjiao/"
            proxies = {"https": "http://182.42.43.176:9077"}
            # user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"
            #user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
            user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0"
            headers = {'User-Agent': user_agent}
            r = requests.get(url,headers=headers,proxies=proxies)
        except Exception,e:
            print e
            return

        #print r.text
        if r.text is not None:
            soup = BeautifulSoup(r.text,'lxml',from_encoding='utf-8')
            for child in soup.find(class_="position").children:
                if type(child.find("div"))== bs4.element.Tag:
                    for link in child.find("div").find_all("a"):
                        # 获取大区域链接
                        new_url = urlparse.urljoin(url,link['href'])
                        # 获取小区域链接
                        try:
                            r = requests.get(new_url,headers,proxies=proxies)
                            soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf-8')
                            for child in soup.find(class_="position").children:
                                if type(child.find("div")) == bs4.element.Tag:
                                    if len(child.find("div").find_all("div")) > 0:
                                        for area_link in child.find("div").find_all("div")[1].find_all("a"):
                                            area_url = urlparse.urljoin(new_url,area_link['href'])
                                            # print area_url
                                            # 爬取小区域分页链接
                                            spider.spider_list_url(area_url)
                        except Exception,e:
                            print e.message
        else:
            print 'content is null !'

    def spider_list_url(self,url):

        # user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0"
        # user_agent = {"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0"}
        headers = {'User-Agent': user_agent}
        proxies = {"https": "http://182.42.43.176:9077"}
        r = requests.get(url, headers=headers,proxies=proxies)
        soup = BeautifulSoup(r.text,'lxml',from_encoding='utf-8')
        # rows = []
        # 爬取分页数据列表
        if soup.find(class_="page-box house-lst-page-box") is not None:
            # print soup.find_all("div",class_="page-box house-lst-page-box")[0]
            page_data = soup.find_all("div",class_="page-box house-lst-page-box")[0]['page-data']
            page_url = soup.find_all("div",class_="page-box house-lst-page-box")[0]['page-url']
            title = ""
            detail_url = ""
            deal_date = ""
            longitude = ""
            latitude = ""

            try:
                if int(json.loads(page_data).get("totalPage")) > 0:
                    for i in range(int(json.loads(page_data).get("totalPage"))):
                    #print page_url,i+1
                        new_url = urlparse.urljoin(url,re.sub(r"{page}",str(i+1),page_url))
                        # 爬取房源信息详情页
                        r = requests.get(new_url, headers=headers,proxies=proxies)
                        soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf-8')
                        # print soup.prettify()
                        if len(soup.find_all(class_="listContent")) > 0:
                            for each in soup.find_all(class_="listContent")[0].find_all("li"):
                                if len(each.find_all("div", class_="info")) == 1 :
                                    title = each.find_all("div", class_="info")[0].find(class_="title").a.string
                                    detail_url = each.find_all("div", class_="info")[0].a['href']
                                #position_info1 = each.find_all("div", class_="flood")[0].find(class_="positionInfo").contents[1]
                                #position_info2 = each.find_all("div", class_="address")[0].find(class_="houseInfo").contents[1]
                                if len(each.find_all("div", class_="address")) == 1:
                                    deal_date = each.find_all("div", class_="address")[0].find(class_="dealDate").string
                                if len(each.find_all("div", class_="flood")) == 1:
                                    price = each.find_all("div", class_="flood")[0].find(class_="unitPrice").find(class_="number").string
                                print title,',', price,',',deal_date,',',detail_url
                                content = (title, price, deal_date, detail_url)
                                if len(content) == 4:
                                    try:
                                        conn = sqlite3.connect('E:/tuotuo/dbdata/gz_lianjia_link.db')
                                    # 创建sqlite数据库
                                        cur = conn.cursor()
                                        cur.execute(' INSERT INTO gz_lianjia_link VALUES (?,?,?,?)',content)
                                        conn.commit()
                                        conn.close()
                                    except Exception, e:
                                        print e
                                # TODO 爬取经纬度
                                location = spider.spider_position_info(detail_url)
                                #if len(location) == 2:
                                #    longitude = location[0]
                                #    latitude = location[1]
                                #print title,',',price,',',longitude,',',latitude,',',deal_date,',',detail_url
                                #content = (title,price,longitude,latitude,deal_date,detail_url)
                                # rows.append(content)
                                #if len(content) == 6:
                                #    try:
                                #        conn = sqlite3.connect('E:/tuotuo/dbdata/gz_lianjia.db')
                                        # 创建sqlite数据库
                                #        cur = conn.cursor()
                                #        cur.execute(' INSERT INTO gz_lianjia VALUES (?,?,?,?,?,?)',content)
                                #        conn.commit()
                                #        conn.close()
                                #    except Exception, e:
                                #        print e
                                    #finally:
                                        #time.sleep(5)

            except Exception,e:
                print e


    def create_linkdb(self):
        conn = sqlite3.connect('E:/tuotuo/dbdata/gz_lianjia_link.db')
        # 创建sqlite数据库
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS gz_lianjia_link(house_name VARCHAR(100),price VARCHAR(20),deal_date VARCHAR(20),detail_url VARCHAR(50))')
        conn.close()

    def create_sqlitedb(self):
        conn = sqlite3.connect('E:/tuotuo/dbdata/gz_lianjia.db')
        # 创建sqlite数据库
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS gz_lianjia(house_name VARCHAR(100),price VARCHAR(20),longitude VARCHAR(20),latitude VARCHAR(20),deal_date VARCHAR(20),detail_url VARCHAR(50))')
        conn.close()

    def insert_data(self,content):
        try:
            conn = sqlite3.connect('E:/tuotuo/dbdata/gz_lianjia.db')
            # 创建sqlite数据库
            cur = conn.cursor()
            cur.executemany(' INSERT INTO gz_lianjia VALUES (?,?,?,?,?,?,?,?)',content)
            conn.commit()
            conn.close()
        except Exception,e:
            print e.message

    # 测试爬取列表
    def spider_detail(self):
        url = "https://gz.lianjia.com/chengjiao/dongpu/pg1/"
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"
        headers = {'User-Agent':user_agent}
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.text,'lxml',from_encoding='utf-8')
        spider = spider_chengjiao()
        # print soup.prettify()
        for each in soup.find_all(class_="listContent")[0].find_all("li"):
            title = each.find_all("div",class_="info")[0].find(class_="title").a.string
            position_info1 = each.find_all("div", class_="flood")[0].find(class_="positionInfo").contents[1]
            position_info2 = each.find_all("div",class_="address")[0].find(class_="houseInfo").contents[1]
            deal_date = each.find_all("div",class_="address")[0].find(class_="dealDate").string
            price = each.find_all("div", class_="flood")[0].find(class_="unitPrice").find(class_="number").string
            detail_url = each.find_all("div",class_="info")[0].a['href']
            # print title,'\t',position_info1,'\t',position_info2,'\t',deal_date,'\t',price,'\t',detail_url

            # 解析房屋经纬度
            location = spider.spider_position_info(detail_url)
            longitude = ""
            latitude = ""
            if len(location) == 2:
                longitude = location[0]
                latitude = location[1]
            print title, '\t', price, '\t', longitude, '\t', latitude, '\t', position_info1, '\t', position_info2, '\t', deal_date, '\t', detail_url



    # 解析经纬度
    def spider_position_info(self,url):
        # url = "https://gz.lianjia.com/chengjiao/GZ0001379573.html"
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"
        # user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf-8')
        details = soup.find_all(text=re.compile("resblockPosition"))
        pattern = re.compile(r"(resblockPosition:')(\d+.\d+)(,)(\d+.\d+)'")
        longitude = re.search(pattern, details[0]).group(2)
        latitude = re.search(pattern, details[0]).group(4)
        # print longitude,latitude
        #if len(details) > 0:
        return longitude,latitude


if __name__ == '__main__':
    spider = spider_chengjiao()
    spider.spider_url()
    # spider.spider_detail()
