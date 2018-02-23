# coding:utf8

from flask_migrate import MigrateCommand
from flask_script import Manager, prompt_bool
from scrapy import cmdline

from LaGouSpiderProject.WebServer.WebServer import app, db
from LaGouSpiderProject.WebServer.model import Admin

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)


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


@manager.option('-a', '--account', dest='account', help='admin login account')
@manager.option('-p', '--pwd', dest='pwd', help='admin login password')
def create_admin(account, pwd):
    admin = Admin(account=account, password=pwd)
    admin.save()

    admin_count = Admin.query.filter_by(account=account).count()
    if admin_count > 0:
        print('create admin success')
    else:
        print('create admin failed')


@manager.command
def drop_all_db():
    if prompt_bool("Are you sure you want to drop all db"):
        db.drop_all()
        print 'completed all db'


if __name__ == '__main__':
    manager.run()
