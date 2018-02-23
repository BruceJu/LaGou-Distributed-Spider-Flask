# coding:utf8

from flask_script import Manager
from scrapy import cmdline
from LaGouSpiderProject.WebServer.WebServer import app

manager = Manager(app=app)


@manager.option('-host', '--host', dest='host', help='run server host', default='127.0.0.1')
@manager.option('-port', '--port', dest='port', help='run server port', default=5000)
def runserver(host, port):
    app.run(host=host, port=port)


@manager.option('-debug', '--debug', dest='debug', help='is debug ??', default=1)
def runspider(debug):
    if debug == 0:
        cmdline.execute('scrapy crawl LGSpider -o data.json -t json'.split())
    else:
        cmdline.execute('scrapy crawl LGSpider'.split())


if __name__ == '__main__':
    manager.run()
