# coding:utf8

from flask import Flask
import WebConfig
from exts import db
from flask_migrate import Migrate
from model import Admin


app = Flask(__name__)
app.config.from_object(WebConfig)
db.init_app(app)
migrate = Migrate(app=app,db=db)


@app.route('/')
def index():
    return 'hello Spider'


if __name__ == '__main__':
    app.run()
