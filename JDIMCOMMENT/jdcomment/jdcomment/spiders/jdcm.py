# -*- coding: utf-8 -*-
import scrapy
import csv
import json
from ..items import JdcommentItem
import win_unicode_console
win_unicode_console.enable()
n=1
goods_info = []
with open('./jdgoods.csv', 'r', encoding='utf-8')as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        if row:
            goods_info.append({'id':row[0],'title':row[1]})

class JdcmSpider(scrapy.Spider):
    name = 'jdcm'
    # allowed_domains = ['sclub.jd.com']
    # start_urls = []

    def start_requests(self):
        for goods in goods_info:
            base_url = 'https://sclub.jd.com/comment/productPageComments.action?productId={}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'.format(goods['id'])
            yield scrapy.Request(base_url,meta=goods,callback=self.parse_page)

    def parse_page(self, response):
        global n
        if 'comments' in response.text:
            data = json.loads(response.text)
            for item in data['comments']:
                comments_info = JdcommentItem()
                comments_info['id'] = response.meta['id']
                comments_info['title']=response.meta['title']
                comments_info['username']=item['nickname']
                comments_info['userid']=item['id']
                comments_info['userLevelName']=item['userLevelName']
                comments_info['referenceName']=item['referenceName']
                comments_info['referenceTime']=item['referenceTime']
                comments_info['content']=item['content']
                comments_info['creationTime']=item['creationTime']
                comments_info['score']= item['score']
                yield comments_info

            if data['comments']:
                next_url = 'https://sclub.jd.com/comment/productPageComments.action?productId={}&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'.format(response.meta['id'],n)
                n+=1
                yield scrapy.Request(next_url,meta=response.meta,callback=self.parse_page)

