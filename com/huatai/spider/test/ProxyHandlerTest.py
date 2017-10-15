#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-10-11 16:49:07
# @File : ProxyHandlerTest.py
# @Software : PyCharm
import urlparse

import bs4
import requests
from bs4 import BeautifulSoup
#from requests.adapters import HTTPAdapter
#requests.adapters.DEFAULT_RETRIES = 5
proxies = {"https":"180.119.65.152:808"}
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"
headers = {'User-Agent': user_agent}
url = "https://gz.lianjia.com/xiaoqu/"
r = requests.get(url,headers=headers, proxies=proxies)
print r.text
#r = requests.get("http://www.lianjia.com",headers)




#print r.content