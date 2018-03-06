# -*- coding: utf-8 -*-

import MySQLdb as mdb



if __name__ == '__main__':
    # 也可以使用关键字参数
    conn = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='woshi007008', db='spiderdata', charset='utf8')
    cursor = conn.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM lagou_job"
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    degree_need_list = []
    final_degree_need_list = []
    '''
    { "name": "大专","y": 45.0,"sliced": "true"}
    '''
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


    series = [
        {
            "type": "pie",
            "name": "学历占比",
            "data": final_degree_need_list
        }
    ]
    print(series)







