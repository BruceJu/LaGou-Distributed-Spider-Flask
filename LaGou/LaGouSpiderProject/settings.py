# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
WEBKIT_DIR = os.path.join(BASE_DIR, 'WebKit')

BOT_NAME = 'LaGouSpiderProject'

SPIDER_MODULES = ['LaGouSpiderProject.spiders']
NEWSPIDER_MODULE = 'LaGouSpiderProject.spiders'


ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 5
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16
COOKIES_ENABLED = False

# 是否使用Webkit来执行动态加载
DYNAMIC_CRAWL = True

RANDOM_UA_TYPE = "random"

# # 分布式配置项目
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# DUPEFILTER_DEBUG = False
# SCHEDULER_FLUSH_ON_START = False
# SCHEDULER_IDLE_BEFORE_CLOSE = 20
# # Don't cleanup redis queues, allows to pause/resume crawls.
# SCHEDULER_PERSIST = True

DOWNLOADER_MIDDLEWARES = {
    'LaGouSpiderProject.middlewares.RandomUserAgentMiddlware': 543,
    'LaGouSpiderProject.middlewares.DynamicCrawlMiddleware': 540,
}

# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }


# ITEM_PIPELINES = {
#    'LaGouSpiderProject.pipelines.JsonWithEncodingPipeline': 300,
# }

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'www.lagou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}
