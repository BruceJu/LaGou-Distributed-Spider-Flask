# -*- coding: utf-8 -*-
import scrapy


class LgspiderSpider(scrapy.Spider):
    name = 'LGSpider'
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/']

    def parse(self, response):
        pass
