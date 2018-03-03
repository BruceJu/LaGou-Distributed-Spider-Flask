# coding:utf8

from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from exts import db


# 管理员
class Admin(db.Model):
    def __init__(self, account, password):
        self.account = account
        self.pwd = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def check_pwd(self, password):
        return check_password_hash(self.pwd, password)

    def __repr__(self):
        return '<Admin %r>' % self.account

    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())


# 拉钩爬虫职位数据
class lagou_job(db.Model):
    __tablename__ = "lagou_job"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), nullable=False, unique=True)
    salary = db.Column(db.String(50), nullable=False)
    job_city = db.Column(db.String(100), nullable=False)
    work_years = db.Column(db.String(100), nullable=False)
    degree_need = db.Column(db.String(50), nullable=False)
    job_type = db.Column(db.String(30), nullable=False)
    publish_time = db.Column(db.DATETIME, default=datetime.now(),nullable=False)
    job_advantage = db.Column(db.String(255), nullable=False)
    job_desc = db.Column(db.TEXT, nullable=False)
    job_addr = db.Column(db.String(255), nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    company_url = db.Column(db.String(255), nullable=False)
    tags = db.Column(db.String(255), nullable=False)
    crawl_time = db.Column(db.DATETIME, default=datetime.now(), nullable=False)

    def __repr__(self):
        return '<lagou_job %r>' % self.url
