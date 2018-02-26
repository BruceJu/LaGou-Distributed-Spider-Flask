# -*- coding: utf-8 -*-
import os
from datetime import datetime
import scrapy
from scrapy import signals
from scrapy.exceptions import CloseSpider, IgnoreRequest
from scrapy.http import Request
from scrapy.xlib.pydispatch import dispatcher
from selenium import webdriver
from LaGou.LaGouSpiderProject.items import LagouJobItemLoader, LagouJobItem


class LgspiderSpider(scrapy.Spider):
    name = 'LGSpider'
    allowed_domains = ['lagou.com']
    start_urls = [
        #"https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?px=default&city=%E6%9D%AD%E5%B7%9E"
        "https://www.lagou.com/jobs/2735005.html"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url,callback=self.detail_page_data)

    def __init__(self, callbackUrl=None, **kwargs):
        super(LgspiderSpider, self).__init__()
        dispatcher.connect(self.spider_open_receiver, signals.spider_opened)
        dispatcher.connect(self.spider_closed_receiver, signals.spider_closed)

    def spider_open_receiver(self):
        self.logger.info('Notice!! !!!Spider is start')
        self.webkit_dir = self.crawler.settings.get("WEBKIT_DIR", "Error")
        self.webkit = os.path.join(self.webkit_dir, r'phantomjs-2.1.1-windows\bin\phantomjs.exe')
        self.logger.info('Notice!! !!!Init webkit from dir %s' % self.webkit)
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap["phantomjs.page.settings.resourceTimeout"] = 1000
        cap["phantomjs.page.settings.loadImages"] = False
        cap["phantomjs.page.settings.disk-cache"] = True
        cap[
            "phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0"
        cap[
            "phantomjs.page.customHeaders.User-Agent"] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'
        self.driver = webdriver.PhantomJS(executable_path=self.webkit, desired_capabilities=cap)
        self.driver.capabilities.update()

    def spider_closed_receiver(self):
        self.logger.info('Notice!! Spider is closed')
        if self.driver is not None:
            self.driver.quit()

    def parse(self, response):
        '''
        拉钩网的职位列表信息中，第一条数据与其他的条目数据是不同的，这里需要注意
        :param response:
        :return:
        '''

        if response.status is not 200:
            raise CloseSpider()

        # 解析职位列表中第一条数据并生成请求
        xpath_div_first_li_position = response.xpath(
            '//div[@class="s_position_list "]/ul[@class="item_con_list"]/li[@class="con_list_item first_row default_list"]')

        first_position_address_link_list = xpath_div_first_li_position.xpath(
            './div[@class="list_item_top"]/div[@class="position"]/div[@class="p_top"]/a[@class="position_link"]/@href').extract()

        for detail_first_page_url in first_position_address_link_list:
            yield Request(url=detail_first_page_url, callback=self.detail_page_data)

        # 解析职位列表中其余的数据，并生成请求
        xpath_default_li_posittion = response.xpath(
            '//div[@class="s_position_list "]/ul[@class="item_con_list"]/li[@class="con_list_item default_list"]')
        value_default_page_link_list = xpath_default_li_posittion.xpath(
            './div[@class="list_item_top"]/div[@class="position"]/div[@class="p_top"]/a[@class="position_link"]/@href').extract()
        print value_default_page_link_list
        for default_detail_page_link in value_default_page_link_list:
            yield Request(url=default_detail_page_link, callback=self.detail_page_data)

    def detail_page_data(self, response):
        if response.status is not 200:
            raise IgnoreRequest()

        # 解析拉勾网的职位
        item_loader = LagouJobItemLoader(item=LagouJobItem(), response=response)
        item_loader.add_css("title", ".job-name::attr(title)")
        item_loader.add_value("url", response.url)
        # item_loader.add_value("url_object_id", common.get_md5(response.url))
        item_loader.add_css("salary", ".job_request .salary::text")
        item_loader.add_xpath("job_city", "//*[@class='job_request']/p/span[2]/text()")
        item_loader.add_xpath("work_years", "//*[@class='job_request']/p/span[3]/text()")
        item_loader.add_xpath("degree_need", "//*[@class='job_request']/p/span[4]/text()")
        item_loader.add_xpath("job_type", "//*[@class='job_request']/p/span[5]/text()")

        item_loader.add_css("tags", '.position-label li::text')
        item_loader.add_css("publish_time", ".publish_time::text")
        item_loader.add_css("job_advantage", ".job-advantage p::text")
        item_loader.add_css("job_desc", ".job_bt div")
        item_loader.add_css("job_addr", ".work_addr")
        item_loader.add_css("company_name", "#job_company dt a img::attr(alt)")
        item_loader.add_css("company_url", "#job_company dt a::attr(href)")
        item_loader.add_value("crawl_time", datetime.now())

        job_item = item_loader.load_item()

        return job_item
