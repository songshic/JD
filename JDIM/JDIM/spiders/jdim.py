# -*- coding: utf-8 -*-
from ..items import JdimItem
import scrapy
from selenium import webdriver
import win_unicode_console
win_unicode_console.enable()

class JdimSpider(scrapy.Spider):
    name = 'jdim'
    # allowed_domains = ['jd.com']
    def __init__(self):
        self.driver=webdriver.Chrome()
        super(JdimSpider, self).__init__()

        # dispatcher.connect(self.closeSpider, signals.spider_closed)

    def closed(self, spider):
        print("spider closed")
        self.driver.close()

    def start_requests(self):
        start_urls = ['https://search.jd.com/Search?keyword=%E8%BF%9B%E5%8F%A3%E7%89%9B%E5%A5%B6&enc=utf-8&wq=%E8%BF%9B%E5%8F%A3%E7%89%9B%E5%A5%B6&pvid=blr7o4wi.ri9kq2']
        yield scrapy.Request(start_urls[0],callback=self.parse_page)

    def parse_page(self, response):
        goodslist = response.css('#J_goodsList > ul > li')
        for info in goodslist:
            id = info.css('li::attr(data-pid)').extract_first()
            title = ''.join(info.xpath('.//div[@class="p-name p-name-type-2"]/a/em//text()').extract())
            price = info.xpath('.//div[@class="p-price"]/strong/i/text()').extract_first()
            url = info.xpath('.//div[@class="p-name p-name-type-2"]/a/@href').extract_first()
            shop = info.xpath('.//div[@class="p-shop"]/span[@class="J_im_icon"]/a/text()').extract_first()
            comment = info.xpath('.//div[@class="p-commit"]/strong/a/text()').extract_first()
            data = JdimItem()
            data['id'] = id
            data['title'] = title
            data['price'] = price
            data['url'] = url
            data['shop'] = shop
            data['comment'] = comment
            yield data