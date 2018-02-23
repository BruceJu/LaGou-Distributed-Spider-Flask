# coding:utf8

from datetime import datetime
from werkzeug.security import generate_password_hash
from exts import db


# 管理员
class Admin(db.Model):
    def __init__(self, account, password):
        self.account = account
        self.pwd = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Admin %r>' % self.account

    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())
