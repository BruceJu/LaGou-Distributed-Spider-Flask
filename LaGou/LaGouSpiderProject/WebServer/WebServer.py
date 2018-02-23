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
