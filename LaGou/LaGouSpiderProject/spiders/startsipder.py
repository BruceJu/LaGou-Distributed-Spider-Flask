# coding:utf8

from scrapy import cmdline


if __name__ == '__main__':
    cmdline.execute('scrapy crawl LGSpider -o data.json -t json'.split())

