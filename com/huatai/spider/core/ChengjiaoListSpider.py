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
import types

class spider_chengjiao(object):

    def spider_url(self):
        spider = spider_chengjiao()
        url = "https://gz.lianjia.com/chengjiao/"
        #user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0"
        headers = {'User-Agent': user_agent}
        r = requests.get(url,headers=headers)

        #print r.text
        if r.text is not None:
            soup = BeautifulSoup(r.text,'lxml',from_encoding='utf-8')
            for child in soup.find(class_="position").children:
                try:
                    if type(child.find("div"))== bs4.element.Tag:
                        for link in child.find("div").find_all("a"):
                            # 获取子大区域链接
                            new_url = urlparse.urljoin(url,link['href'])
                            # 获取子小区域链接
                            r = requests.get(new_url,headers)
                            soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf-8')
                            for child in soup.find(class_="position").children:
                                if type(child.find("div")) == bs4.element.Tag:
                                    for area_link in child.find("div").find_all("div")[1].find_all("a"):
                                        finally_url = urlparse.urljoin(new_url,area_link['href'])
                                        #print finally_url
                                        spider.spider_list_url(finally_url)
                except Exception,e:
                    print e.message
        else:
            print 'content is null !'

    def spider_list_url(self,url):
        # user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0"
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text,'lxml',from_encoding='utf-8')

        if soup.find(class_="page-box fr") is not None:
            # print soup.find(class_="page-box house-lst-page-box").children
            for child in soup.find(class_="page-box fr").children:
                if type(child) == bs4.element.Tag:
                    print type(child.find_all("div"))
                    print child.find_all("div")


if __name__ == '__main__':
    spider = spider_chengjiao()
    spider.spider_url()
