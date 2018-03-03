# -*- coding: utf-8 -*-


BOT_NAME = 'LaGouSpiderProject'

SPIDER_MODULES = ['LaGouSpiderProject.spiders']
NEWSPIDER_MODULE = 'LaGouSpiderProject.spiders'

ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

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
    # 'LaGouSpiderProject.middlewares.RandomProxyMiddleware': 541,
      'LaGouSpiderProject.middlewares.RandomUserAgentMiddlware': 542,
    # 'LaGouSpiderProject.middlewares.DynamicCrawlMiddleware': 545,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 543,
}

ITEM_PIPELINES = {
   #'LaGouSpiderProject.pipelines.JsonWithEncodingPipeline': 300,
   'LaGouSpiderProject.pipelines.MysqlTwistedPipline': 300,
}


# 防ban操作
DOWNLOAD_DELAY = 10

# AUTOTHROTTLE_ENABLED = True
#
# AUTOTHROTTLE_START_DELAY = 10
# AUTOTHROTTLE_MAX_DELAY = 20
# AUTOTHROTTLE_DEBUG = True

# MySQL数据库连接
MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "spiderdata"
MYSQL_USER = "root"
MYSQL_PASSWORD = "woshi007008"