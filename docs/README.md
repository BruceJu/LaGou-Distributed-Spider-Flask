<style>
.div-border-image{
    margin-top: 20px;
    margin-bottom: 10px;
    box-shadow: 10px 10px 5px #888888;
    width:100%;
    hegiht:auto;
    background: whitesmoke;
    border: yellowgreen inset;
    border-right-width: 0px;
    border-top-width: 0px;
    border-bottom-width: 0px;
    border-left-width: 5px;
    border-radius: 5px;
    }
.div-border-question{
    margin-top: 20px;
    margin-bottom: 10px;
    box-shadow: 10px 10px 5px #888888;
    width:100%;
    hegiht:50px;
    padding:20px;
    background: whitesmoke;
    border: red inset;
    border-right-width: 0px;
    border-top-width: 0px;
    border-bottom-width: 0px;
    border-left-width: 5px;
    border-radius: 5px;
    }
.div-border-answer{
    margin-top: 20px;
    margin-bottom: 10px;
    box-shadow: 10px 10px 5px #888888;
    width:100%;
    hegiht:50px;
    padding:20px;
    background: whitesmoke;
    border: #4876FF inset;
    border-right-width: 0px;
    border-top-width: 0px;
    border-bottom-width: 0px;
    border-left-width: 5px;
    border-radius: 5px;
    }       
</style>
# LaGou-Distributed-Spider-Flask

----
[toc]

<div class="div-border-answer">
分布式采集拉钩网中杭州爬虫相关职位的数据并使用Flask进行数据的可视化与分析
</div>


## 写在前面
<div class="div-border-answer">
来北京3年多了，这3年来，经历了很多了，成长了很多，领悟了许多，也看懂了很多，但是居京都大不易，来北京之前也没有
考虑过在北京定居这个想法，现在也依然没有，即便我有能力在这里定居，我也不会在这里定居，原因就是我不喜欢这个城市
，这里太过于喧嚣，太过于吵闹，就像唐寅那句，‘车尘马足富者趣，酒盏花枝贫者缘。’，北京，于我来说，终究是个临时的
泊岗，而我于北京，终究是个过客，既然迟早要离开，而现在又赶上现在的这样的一个机会，所以，再见，北京。
</div>

## 项目概述

<div class="div-border-question">
好了，说回这个项目，因为之前一直做的是数据采集的相关的工作，以前是通过SDK的方式来采集数据，由于工作的需要，便学习了
网络爬虫，从刚刚开始的定向爬虫，到后来的多机分布式爬虫，定时服务化爬虫，可视化爬虫，在爬虫的使用上，还是有丰富的经验的
现在要离开北京，去杭州了，主要想要从数据采集相关的工作，所以便萌生了一个想法，用爬虫，爬取以下有关数据采集的相关数据，
并进行一下分析，在用 `Flask` 进行一下可视化，为啥要选Flask那，因为它轻啊，`Django` 太过于繁重了，用于中级以上的项目来说是个不
错的选择，但是对于个人来说，Flask是个不二的选择。
</div>

> - [x] 支持分布式采集

*
> - [x] SemanticUi+Flask数据可视化

*
> - [x] 提供登录权限认证功能

*
> - [x] 支持flask_script 命令管理

*
> - [x] 支持flask_sqlalchemy数据库orm映射

*
> - [x] 支持动态抓取

*
>- [x] 支持异常状态收集，与重试

*
>- [x] 支持运行状态的邮件通知



## 项目结构

* 在整体结构上涉及三个部分，
   * 数据采集
   * 数据存储
   * 数据分析与可视化

### 数据采集
 在数据采集上，准备使用 `Scrapy-Redis`和`Redis`来实现多机器分布爬取,目标网站是拉钩网，由于拉钩网的反爬
 还是比较严厉的，所以需要进行一下防ban的操作，具体的实现我会写在下面

### 数据存储
 在数据存储上，前期分析了一下，数据大约几百条，不到1000条，所以就不用需要分布式存储了，直接用`MySQL`或者是`MongDB`存储一下就好了，
 可以先把数据同步在`Redis`中，然后在写个脚本直接从`Redis`同步到MySQL中，就不考虑`Redis`磁盘存储了，或者直接放在磁盘上，就不放在内存中了，
 也方便`Flask`使用。  

### 数据分析与可视化
 在数据可视化上，准备使用`Flask`来实现一个`WebServer`,因为Flask比较轻，所以我非常喜欢`Flask`，基于插件，想要什么功能
 直接用插件来实现即可。用`Flask`来进行数据的可视化，可以分析一下，杭州各个区的数据采集相关的职位数量，薪资和工作年限的分布清空
 或者统计一下，在任职需求中出现频率最高的词汇 Top10等等
 
 ### 补充说明
  最近接触了一个非常不错的文档在线生成工具，[docsify](https://docsify.js.org/#/),这个工具非常的不错，使用GitHubPage可以直接完成部署的工作，非常方便，vue风格的界面非常美观
  对于我这种经常写文档的同学来说，简直是天大的福音。我的这个项目，会提供一份说明文档。就使用这个 [docsify](https://docsify.js.org/#/)来实现，
  最后会呈现在[LaGou-Distributed-Spider-Flask项目说明文档](https://bruceju.github.io/LaGou-Distributed-Spider-Flask/)
   * Python 版本；Python 2.7
   * Scrapy 版本: Scrapy 1.5.0
   * Redis 系统版本： Windows 64bit  Redis-x64-3.2.100

## 构建Flask



### 创建Flask

 这个没有什么太特别的地方
 
 ```python
# coding:utf8

from flask import Flask

import WebConfig

app = Flask(__name__)

app.config.from_object(WebConfig)


@app.route('/')
def index():
    return 'hello Spider'


if __name__ == '__main__':
    app.run()

```

### 构建命令行操作

> 为了能在cmd/shell中控制WebServer和Spider，需要设计几个操作命令，使用的是`flask_script`
 * 提供以下几个命令
   * db init (数据库初始化)
   * create_admin -a <帐户名> - p <密码> 
       * 用于向数据库种添加Admin，用于登录WebServer
       * 需要使用者 在命令行中进行输入，并加密储存
   * runserver -host <帐户名> -port <密码> (启动WebServer)
       * 接受用户输入的 host 和 port 进行host和port设置
       * 默认是在 host=127.0.0.1 port = 5000 下运行
   * runspider -debug <是否是调试模式> (启动Spider)
       * 模式模式下，会自动将爬取的数据输出到 data.json文件中 
   * drop_all_db 重置数据库，进行信息提示，需要用户输入确认信息才能执行。    
       
 * 由于进行到此时，还没有进行db相关操作，所有先实现  `runserver`和 `runspider`的俩个部分的逻辑，
 * 这里要注意项目的目录结构，否则会出现问题，可以参考d代码中的目录结构
 * 在根目录创建 一个 `Manager.py`这样的一个文件用于命令的管理 部分代码如下

```python
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
```

### 创建数据库模块
> 思考过后，决定使用MySQL了，那么现在需要创建一个数据库和一个管理员的表，这里使用的是
``flask_sqlalchemy`` 进行数据库关系的映射
  * 使用`flask_sqlalchemy`连接MySQL数据库模块
  * 创建Admin的class进行管理员的数据模表的映射
  
* 使用 `flask_sqlalchemy` 连接数据库，这里为了避免循环引用的问题
* 创建了一个类`exts.py`来进行间接引用,然后在WebServer中进行初始化

```python
 # coding:utf8
'''
exts.py类
'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```
```python 
# coding:utf8

'''
WebServer.py类
'''

from flask import Flask
import WebConfig
from exts import db

app = Flask(__name__)
app.config.from_object(WebConfig)
db.init_app(app)

```
* 创建管理员的数据模型 创建一个 `model.py`来存放所有的数据表模型,应该存在以下字段
  * 表名 `admin`
  * id 整形，主键，自增长
  * account 字符串，不重复
  * pwd 字符串，不重复，需要加密
  * addtime 时间类型，自动获取
  * 封装 ``save()``操作
  
```python
# coding:utf8

'''
model.py类
'''

from datetime import datetime
from werkzeug.security import generate_password_hash
from exts import db


# 管理员
class Admin(db.Model):

    __tablename__ = 'admin'
 
    def __init__(self, account, password):
        self.account = account
        self.pwd = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Admin %r>' % self.account

   
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())
```  

### 生成数据库
> 这里本来可以使用 `db.create_all()`来进行数据库的同步，但是这样不利于数据库的升级和迁移操作
所以为了一劳永逸，还是使用 ``flask_migrate`` 来进行数据库的映射和修改，迁移操作。

* 初始化 ``flask_migrate``
* 导入数据模型的类
* 运行python Manager.py db init 进行数据库的初始化
* 再运行python Manager.py db migrate 进行数据库的迁移
* 运行python Manager.py db upgrade 进行数据库的更新
* 成功后目前下会有一个 `migrations`的目录
* 这个是记录迁移数据库的版本西信息的不要删除，如下图
* 数据库中应该有俩个表，如下图
<div class="div-border-image">
![001](https://thumbnail0.baidupcs.com/thumbnail/ab3a0cdb0e98edfe13edafc133ba6bcd?fid=3180846231-250528-830986105675917&time=1519455600&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-wmKXLoAE%2F%2BV1pxikmhCDvhqeFrA%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=1267063311391768909&dp-callid=0&size=c710_u400&quality=100&vuk=-&ft=video)
</div>
* 部分代码如下

```python

# coding:utf8
'''
 WebServer.py 类
'''

from flask import Flask
import WebConfig
from exts import db
from flask_migrate import Migrate
from model import Admin


app = Flask(__name__)
app.config.from_object(WebConfig)
db.init_app(app)
migrate = Migrate(app=app,db=db)
```
```python
# coding:utf8
'''
 Manager.py 类
'''
from LaGouSpiderProject.WebServer.WebServer import app
from LaGouSpiderProject.WebServer.model import Admin

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

```
### 注意
<div class="div-border-question">
<p style="color:red;font-size:7">注意</p>
 * 我在进行数据库的`init`命令时，我之前这个数据库中的所有数据表都被删除了
 * 好在我这里的数据不是很多
 * 所以在使用`db init`命令时，要保证数据库是空的
</div>

### 提供管理员添加命令
> 现在数据库有了，那么就可以针对admin表进行cmd命令的设计了,代码如下

```python
'''
Manager.py
'''
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
```
* 效果如下

<div class="div-border-image">
![avatar](https://thumbnail0.baidupcs.com/thumbnail/1583eaf9cd2b888a8c904d4f32b0e255?fid=3180846231-250528-546478717734915&time=1519455600&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-%2ByaR3iELK9Z0347NugMSOAHQIF0%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=1267047199009381481&dp-callid=0&size=c710_u400&quality=100&vuk=-&ft=video)
</div>
 


### 登录认证

> 现在数据库有了，并且也可以用命令生成Admin角色了，那么就下了可以开始构建登录认证功能了

* 登录认证功能设计思路
  * SemanticUi构建前端页面
  * 使用蓝图构建项目结构
  * flask_wtf设计登录表单
  * 提供输入字段验证
  * 提供消息闪现支持
  * 提供基于登录的访问控制的装饰器
  
```python
# coding:utf8
from functools import wraps

from flask import render_template, redirect, url_for, flash, session, request

from forms import LoginForm
from . import admin
from ..model import Admin


def admin_logon_request(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login' or request.url))
        return function(*args, **kwargs)

    return decorated_function


@admin.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        data = loginForm.data
        record = Admin.query.filter_by(account=data['account']).first()
        if not record.check_pwd(data['pwd']):
            flash('密码错误')
            return redirect(url_for('admin.login'))
        else:
            # 构造session
            session['admin'] = data['account']
            print(session)
            return redirect(url_for('admin.index' or request.args["next"]))

    return render_template('admin/login.html', form=loginForm)


@admin.route('/logout')

def logout():
    session['admin'].pop()
    return redirect(url_for('admin.login'))


@admin.route('/')
@admin_logon_request
def index():
    return 'hello'
```  

* 效果1
<div class="div-border-image">
![001](https://thumbnail0.baidupcs.com/thumbnail/1829a9ee777cf509df4fa8f72ab839fc?fid=3180846231-250528-620318043291499&time=1519459200&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-oVO2TA0bjH3SaTOlLABB%2B%2FaMc5Y%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=1268135052722737272&dp-callid=0&size=c710_u400&quality=100&vuk=-&ft=video)
</div>
* 效果2
<div class="div-border-image">
![001](https://thumbnail0.baidupcs.com/thumbnail/781e591ebce098e31ad671db4bda5ddf?fid=3180846231-250528-908421849970235&time=1519459200&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-%2BJa9lAwO718%2BTZRecIbo0Bri8mY%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=1268108100717009770&dp-callid=0&size=c710_u400&quality=100&vuk=-&ft=video)
</div>


## 构建爬虫

### 创建爬虫

* 使用`Scrapy`创建一个项目并进行爬虫编译 ，使用的命令是 
 
```Scrapy
scrapy startproject <项目名>
scrapy genspider <爬虫名字> <允许访问的主机地址>
```

### 防Ban操作

#### 添加随机UA操作

> useragent ，request_header这是网页对于访问者的验证，在爬虫中需要设置UserAgent，否则部分网络将无法爬取

* 使用第三方随机UA的库
* 添加中间件，进行UA的随机切换
* 代码如下

```python
# -*- coding: utf-8 -*-
from fake_useragent import UserAgent

class RandomUserAgentMiddlware(object):
    # 随机更换user-agent
    def __init__(self, crawler):
        super(RandomUserAgentMiddlware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        # 当每个request通过下载中间件时，该方法被调用。
        def get_ua():
            return getattr(self.ua, self.ua_type)
        request.headers.setdefault('User-Agent', get_ua())

```

### 添加针对JS的抓取支持

> 由于拉钩网的页面都是是用js来加载数据的，所有这里需要使用一种方式来处理JS，其实方式有很多，这里我采用的是``selenium``+``PhantomJS``的方式

* 引入``selenium``和``PhantomJS``
* 编写中间件进行js的处理

```python

import os
import scrapy
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from selenium import webdriver

class LgspiderSpider(scrapy.Spider):
    name = 'LGSpider'
    allowed_domains = ['lagou.com']
    start_urls = [
        "https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?px=default&city=%E6%9D%AD%E5%B7%9E"

    ]

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
        cap["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0"
        cap["phantomjs.page.customHeaders.User-Agent"] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'
        self.driver = webdriver.PhantomJS(executable_path=self.webkit, desired_capabilities=cap)
  

    def spider_closed_receiver(self):
        self.logger.info('Notice!! Spider is closed')
        if self.driver is not None:
            self.driver.quit()
```

* 中间件

```python
from scrapy.http import HtmlResponse


class DynamicCrawlMiddleware(object):

    def __init__(self, crawler):
        super(DynamicCrawlMiddleware, self).__init__()

        self.isDynamic = crawler.settings.getbool('DYNAMIC_CRAWL', False)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        if self.isDynamic:
            spider.driver.capabilities['phantomjs.page.settings.userAgent'] = UserAgent()
            spider.driver.capabilities['phantomjs.page.customHeaders.User-Agent'] = UserAgent()
            spider.driver.get(request.url)
            import time
            time.sleep(2)
            spider.logger.info("load url for WebKit:{0}".format(spider.driver.current_url))
            return HtmlResponse(url=spider.driver.current_url, body=spider.driver.page_source, encoding="utf-8",request=request)

```

```python

'''
setting.py
'''

# 是否使用Webkit来执行动态加载
DYNAMIC_CRAWL = True

RANDOM_UA_TYPE = "random"

DOWNLOADER_MIDDLEWARES = {
    'LaGouSpiderProject.middlewares.RandomUserAgentMiddlware': 543,
    'LaGouSpiderProject.middlewares.DynamicCrawlMiddleware': 540,
}

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'www.lagou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}

```

### 定义条目加载器

* 定义解析字段，定义架加载器
* 字段如下
```python

import scrapy

class LagouJobItem(scrapy.Item):
    # 拉勾网职位信息
    title = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    salary = scrapy.Field()
    job_city = scrapy.Field()
    work_years = scrapy.Field()
    degree_need = scrapy.Field()
    job_type = scrapy.Field()
    publish_time = scrapy.Field()
    job_advantage = scrapy.Field()
    job_desc = scrapy.Field()
    job_addr = scrapy.Field()
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    tags = scrapy.Field()
    crawl_time = scrapy.Field()
```

### 进行数据提取

> 数据提取这里，要使用 `Xpath`和`Css`选择器来进行数据的解析具体的解析规则如下

* 编写解析规则
* 进行数据解析

```python
from datetime import datetime
from scrapy.exceptions import CloseSpider, IgnoreRequest
from scrapy.http import Request

from LaGou.LaGouSpiderProject.items import LagouJobItemLoader, LagouJobItem
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
```
### 数据清洗

> 提出来的数据是不规范的，需要进行一下清洗，需要使用 ``MapCompose, TakeFirst, Join，remove_tags``的函数

* 去空格
* 去网页标签
* 去特殊符号
* 格式化时间

```python
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags
from LaGou.LaGouSpiderProject.Util import common


def formatTime(value):
    # 对抓取的时间进行计算，格式化
    return common.format_time(value)

def remove_splash(value):
    # 去掉工作城市的斜线
    return value.replace("/", "")


def handle_jobaddr(value):
    addr_list = value.split("\n")
    addr_list = [item.strip() for item in addr_list if item.strip() != "查看地图"]
    return "".join(addr_list)


def handle_jobdecs(value):
    decs_list = value.split("\n")
    return "".join(decs_list)
class LagouJobItem(scrapy.Item):
    # 拉勾网职位信息
    title = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    salary = scrapy.Field()
    job_city = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    work_years = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    degree_need = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    job_type = scrapy.Field()
    publish_time = scrapy.Field()
    job_advantage = scrapy.Field()
    job_desc = scrapy.Field(
        input_processor=MapCompose(remove_tags,handle_jobdecs),
    )
    job_addr = scrapy.Field(
        input_processor=MapCompose(remove_tags, handle_jobaddr),
    )
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    tags = scrapy.Field(
        input_processor=Join(",")
    )
    crawl_time = scrapy.Field()    
```

### 清洗后的数据展示

```json
[
    {
        "salary": "10k-20k ",
        "publish_time": "2018-02-25 17:21",
        "tags": "信息安全,Python",
        "url": "https://www.lagou.com/jobs/2735005.html",
        "title": "python",
        "job_type": "全职",
        "job_advantage": "五险一金,带薪年假,节假日福利,国内外旅游",
        "job_city": "杭州 ",
        "company_url": "https://www.lagou.com/gongsi/6462.html",
        "work_years": "经验1-3年 ",
        "company_name": "杭州安恒信息技术有限公司",
        "job_addr": "杭州 -滨江区 -江南- 通和路68号中财大厦15楼",
        "job_desc": "        岗位职责：1.分析产品需求, 并给出良好的解决方案；2.引擎平台功能模块的设计和实现；3. 跟踪和了解网络安全领域最新技术,工具和开源代码；4.现有产品性能,可靠性,可用性的提升；5.处理一些应急的工作。任职资格：1.1年以上的python语言开发经验, 最好有2年及以上面向对象(C++, JAVA, C#,GO等)开发经验；2.熟悉TCP/IP协议及开发, 熟悉ARP,ICMP,HTTP,SSH等基础协议；3.能熟练使用Linux/UNIX操作系统和网络相关指令；4.能从Devops视角把控项目,实现产品的易测性,易部署,易升级；5.具有良好的团队精神和合作意识, 具备良好的沟通和执行力，能快速融入团队；6.有网络安全背景优先。        ",
        "degree_need": "本科及以上 ",
        "crawl_time": "2018-02-26 17:21:12"
    }
]
```


   
    
   
      
 

