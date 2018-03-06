# -*- coding: utf-8 -*-
from functools import wraps

import MySQLdb as mdb
from flask import render_template, redirect, url_for, flash, session, request, Response, json

from forms import LoginForm
from . import admin
from ..model import Admin

conn = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='woshi007008', db='spiderdata', charset='utf8')
cursor = conn.cursor()
# SQL 查询语句
sql = "SELECT * FROM lagou_job"
# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()


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
    return render_template('admin/index.html')


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@admin.route('/job_area_json/', methods=['GET', 'POST'])
def job_area_json():
    area_list = []
    for item in results:
        area_list.append(item[11].split('-')[1].decode('utf-8').strip())
    area_index_list = list(set(area_list))
    # 索引 list
    final_area_index_list = [area for area in area_index_list if len(area) < 9]
    # 数量 list
    # 构造最终数据
    series = []
    for final_area in final_area_index_list:
        serie = {}
        area_count_list = []
        area_count_list.append(area_list.count(final_area))
        serie['data'] = area_count_list
        serie['name'] = final_area
        series.append(serie)
    content = json.dumps(series)
    resp = Response_headers(content)
    return resp


@admin.route('/degree_need_json/', methods=['GET', 'POST'])
def degree_need_json():
    degree_need_list = []
    final_degree_need_list = []

    for item in results:
        degree_need_list.append(item[6].strip())
        degree_need_index_list = list(set(degree_need_list))
        # 构造索引

    for item in degree_need_index_list:
        data = {}
        data['name'] = item
        data['y'] = degree_need_list.count(item)
        data['sliced'] = True
        final_degree_need_list.append(data)

        series ={}
        series["type"] = "pie"
        series["name"] = "学历占比"
        series["data"] = final_degree_need_list
    content = json.dumps(series)
    print content
    resp = Response_headers(content)
    return resp


from wordcloud import WordCloud
import jieba
