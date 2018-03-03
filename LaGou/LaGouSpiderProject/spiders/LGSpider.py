# -*- coding: utf-8 -*-
import json
import time
from datetime import datetime
from scrapy_redis.spiders import RedisSpider

import scrapy
from scrapy.exceptions import CloseSpider, IgnoreRequest
from scrapy.http import FormRequest,Request

from ..items import LagouJobItem,LagouJobItemLoader


class LgspiderSpider(RedisSpider):
    name = 'LGSpider'
    allowed_domains = ['lagou.com']
    start_urls = [
        "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0"
    ]
    detail_page_url_no_format = 'https://www.lagou.com/jobs/{0}.html'

    lagou_list_page_headers = {
        "Host": "www.lagou.com",
        "Connection": "keep-alive",
        "Origin": "https://www.lagou.com",
        "X-Anit-Forge-Code": 0,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "X-Anit-Forge-Token": "None",
        "Referer": "https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?city=%E6%9D%AD%E5%B7%9E&cl=false&fromSearch=true&labelWords=sug&suginput=python",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "_ga=GA1.2.1638132853.1515770228; user_trace_token=20180112231709-a856d4a7-f7ab-11e7-a2de-5254005c3644; LGUID=20180112231709-a856dbb4-f7ab-11e7-a2de-5254005c3644; TG-TRACK-CODE=search_code; JSESSIONID=ABAAABAAADEAAFIF7B6CF46337E5D77E28B8C966304570C; _gid=GA1.2.857854279.1519745895; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1519745895; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1519745895; LGSID=20180227233818-3b8b5737-1bd4-11e8-b0e4-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%25E7%2588%25AC%25E8%2599%25AB%3Fcity%3D%25E6%259D%25AD%25E5%25B7%259E%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3Dsug%26suginput%3Dpython; LGRID=20180227233818-3b8b58aa-1bd4-11e8-b0e4-5254005c3644; SEARCH_ID=f56ddf55a50b4300a856f6b16d22e0b2"
    }

    lagou_detail_page_headers = {
        "Host": "www.lagou.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": 1,
        "Referer": "https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?city=%E6%9D%AD%E5%B7%9E&cl=false&fromSearch=true&labelWords=sug&suginput=python",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "_ga=GA1.2.1638132853.1515770228; user_trace_token=20180112231709-a856d4a7-f7ab-11e7-a2de-5254005c3644; LGUID=20180112231709-a856dbb4-f7ab-11e7-a2de-5254005c3644; TG-TRACK-CODE=search_code; JSESSIONID=ABAAABAAADEAAFIF7B6CF46337E5D77E28B8C966304570C; _gid=GA1.2.857854279.1519745895; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1519745895; LGSID=20180227233818-3b8b5737-1bd4-11e8-b0e4-5254005c3644; index_location_city=%E6%9D%AD%E5%B7%9E; SEARCH_ID=7a1e6f2c7e494978a4ce29636f1e53b8; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1519750862; LGRID=20180228010104-cbb1e056-1bdf-11e8-b0fa-5254005c3644"

    }

    lagou_default_cookie = {
        "_ga": "GA1.2.1638132853.1515770228",
        "user_trace_token": "20180112231709-a856d4a7-f7ab-11e7-a2de-5254005c3644",
        "LGUID": "20180112231709-a856dbb4-f7ab-11e7-a2de-5254005c3644",
        "_gid": "GA1.2.857854279.1519745895",
        "LGSID": "20180227233818-3b8b5737-1bd4-11e8-b0e4-5254005c3644",
        "index_location_city": "%E6%9D%AD%E5%B7%9E",
        "SEARCH_ID": "7a1e6f2c7e494978a4ce29636f1e53b8",
        "JSESSIONID": "ABAAABAAADEAAFIC4CE029BD7C2A97E7D3A46235B0D430A",
        "_gat": "1",
        "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6": "1519745895,1519752695",
        "Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6": "1519752705",
        "LGRID": "20180228013148-16aad05f-1be4-11e8-9591-525400f775ce"
    }

    def start_requests(self):
        for page_url in self.start_urls:
            formdata = {"first": "true", "pn": "1", "kd": "Python爬虫"}
            return [FormRequest(url=page_url, headers=self.lagou_list_page_headers
                                , formdata=formdata, callback=self.parse)]

    def parse(self, response):
        '''
        拉钩网的职位列表信息中，第一条数据与其他的条目数据是不同的，这里需要注意
        :param response:
        :return:
        '''

        if response.status is not 200:
            raise CloseSpider()

        json_data = json.loads(response.text.decode('utf-8'))

        position_data = json_data["content"]["positionResult"]['result']

        for positions in position_data:
            position_id = positions['positionId']
            final_detail_page_url = self.detail_page_url_no_format.format(position_id)
            print(final_detail_page_url)
            yield Request(url=final_detail_page_url, headers=self.lagou_detail_page_headers,
                          callback=self.detail_page_data, cookies=self.lagou_default_cookie)

        # 解析翻页字段，构造下一页的数据请求。
        current_page_number = json_data["content"]["pageNo"]
        total_page_number = json_data["content"]["pageSize"]
        print 'notice!! current page number is {0},and Total page is {1}'.format(current_page_number, total_page_number)
        time.sleep(5)
        if current_page_number <= total_page_number:
            # 生成下一页的数据请求
            next_page_number = current_page_number + 1
            formdata = {"first": "false", "pn": str(next_page_number), "kd": "python爬虫"}
            yield FormRequest(url=self.start_urls[0], headers=self.lagou_list_page_headers, formdata=formdata,
                              callback=self.parse)
        else:
            print('notice!! Complete the capture of all data')

    def detail_page_data(self, response):

        if response.status is not 200:
            raise IgnoreRequest()

        # 解析拉勾网的职位
        item_loader = LagouJobItemLoader(item=LagouJobItem(), response=response)
        item_loader.add_css("title", ".job-name::attr(title)")
        item_loader.add_value("url", response.url)
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
