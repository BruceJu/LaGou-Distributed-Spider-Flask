# -*- coding: utf-8 -*-
import scrapy


class LagouspiderSpider(scrapy.Spider):
    name = 'laGouSpider'
    allowed_domains = ['https://www.lagou.com']
    start_urls = ['http://https://www.lagou.com/']

    def parse(self, response):
        pass
