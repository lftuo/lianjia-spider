#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-10-9 09:26:01
# @File : LianjiaErShouDetailSpider.py
# @Software : PyCharm
# 爬取链家二手房详情页信息
import re
import csv
from _ssl import SSLError

import requests
import sys
import json
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

class DetailSpider(object):

    '''
    获取每套房子详细链接
    '''
    def spider_data(self):
        rows = []
        failed_rows = []
        with open('../../../../data/lianjia_data.csv') as f:
            try:
                f_csv = csv.DictReader(f.read().splitlines())
                for row in f_csv:
                    # print row.get('houseInfo_1'),'\t',row.get('clear_link')
                    title = row.get('title')
                    url = row.get('clear_link')
                    house_name = row.get('houseInfo_1')
                    position_info = row.get('positionInfo_1')
                    if url is None:
                        return
                    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"
                    headers = {'User-Agent': user_agent}
                    try:
                        r = requests.get(url, headers=headers)
                        if r.status_code == 200:
                            r.encoding = 'utf-8'
                            soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf-8')
                            details = soup.find_all(text=re.compile("resblockPosition"))
                            if len(details) > 0:
                                # print re.findall(r"resblockPosition+:'\d+.\d+,\d+.\d+'",details[0].encode('unicode-escape'))
                                price_pattern = re.compile(r"(price:)(')(\d+)(')")
                                price = re.search(price_pattern,details[0]).group(3)

                                #block_pattern = re.compile(r"(resblockName:)(')([\w\u2E80-\u9FFF]+)(')")
                                #block_name = re.search(block_pattern,details[0]).group(0)

                                pattern = re.compile(r"(resblockPosition:')(\d+.\d+)(,)(\d+.\d+)'")
                                longitude = re.search(pattern,details[0]).group(2)
                                latitude = re.search(pattern,details[0]).group(4)
                                content = (title,house_name,price,position_info,longitude,latitude,url)
                                rows.append(content)
                                print title,'\t',house_name,'\t',price,'\t',position_info,'\t',longitude,'\t',latitude,'\t',url
                    except (Exception,SSLError),e:
                        print title,'\t',url,'\t',e.message
                        failed_content = (title,house_name,url,e.message)
                        failed_rows.append(failed_content)
            except Exception, e:
                print e.message
            finally:
                 # 爬取成功的链接
                 headers = ['title','house_name','price','position_info','longitude','latitude','url']
                 with open('../../../../data/lianjia_gz_details.csv', 'w') as f:
                    f_csv = csv.writer(f)
                    f_csv.writerow(headers)
                    f_csv.writerows(rows)
                 # 爬取失败的链接
                 headers = ['title','house_name','url','error_message']
                 with open('../../../../data/lianjia_gz_details_failed.csv', 'w') as f:
                    f_csv = csv.writer(f)
                    f_csv.writerow(headers)
                    f_csv.writerows(failed_rows)


if __name__ == '__main__':
    spider = DetailSpider()
    spider.spider_data()
