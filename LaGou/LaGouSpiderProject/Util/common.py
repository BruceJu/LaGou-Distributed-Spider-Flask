# -*- coding: utf-8 -*-


import hashlib
import json
import random
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import requests

# -*- coding: utf-8 -*-
import hashlib
import re
import datetime


def extract_num(text):
    #从字符串中提取出数字
    match_re = re.match(".*?(\d+).*", text)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums

def get_md5(urls):
    if type(urls) is list:
        url = urls.pop(0)
    if isinstance(url, unicode):
        url = url.encode('utf-8')
    m = hashlib.md5(url)
    m.update(url)
    return m.hexdigest()


def QueryRandomIP(address):
    r = requests.get(url=address)
    ip_ports = json.loads(r.text)
    index = random.randint(0, len(ip_ports) - 1)
    ip = ip_ports[index][0]
    port = ip_ports[index][1]
    proxies = {
        'http': 'http://%s:%s' % (ip, port),
        'https': 'http://%s:%s' % (ip, port)
    }
    return proxies


def sendmail(content, To, Subject):
    if To is not None and len(To) > 0:
        for msgTo in To:
            msg_from = '1198746549@qq.com'  # 发送方邮箱
            passwd = 'zqngiapraoivgaec'  # 填入发送方邮箱的授权码
            msg_to = msgTo  # 收件人邮箱
            message = MIMEText(content, 'plain', 'utf-8')
            message['From'] = Header('LPythonSpider', 'utf-8')
            message['To'] = Header('develop_yangyang@163.com', 'utf-8')
            message['Subject'] = Header(Subject, 'utf-8')
            try:
                s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
                s.login(msg_from, passwd)
                s.sendmail(msg_from, msg_to, message.as_string())
                print "发送成功"
            except smtplib.SMTPException, e:
                print "发送失败"
            finally:
                s.quit()

def format_time(text):
    # 对抓取的时间进行计算，格式化
    if '分钟' in text:
        return (datetime.datetime.now() - datetime.timedelta(minutes=extract_num(text))).strftime("%Y-%m-%d %H:%M")
    elif '小时'in text:
        return (datetime.datetime.now() - datetime.timedelta(hours=extract_num(text))).strftime("%Y-%m-%d %H:%M")
    elif '天'in text:
        return (datetime.datetime.now() - datetime.timedelta(days=extract_num(text))).strftime("%Y-%m-%d %H:%M")
    elif '周'in text:
        return (datetime.datetime.now() - datetime.timedelta(weeks=extract_num(text))).strftime("%Y-%m-%d %H:%M")
    else:
        str_time= re.compile('[0-9]{4}[-][0-9]{1,2}[-][0-9]{1,2}[0-9]{1,2}[:][0-9]{1,2}').findall(text).pop()
        return datetime.datetime.strptime(str_time,'%Y-%m-%d%H:%M')

if __name__ == '__main__':
    print format_time('1天前  发布于拉勾网')
    print format_time('1小时之前')
    print format_time('2天之前')
    print format_time('5周之前')
    print format_time('2017-10-0513:55发表了文章')


