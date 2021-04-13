# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 21:49
# @Author  : sunnysab
# @File    : query.py
#  使用方法:
#  1. 运行 flask run query.py
#  2. 向 localhost:5000/query 发送 post 请求，请求体参数为
#     - week  周数，数字
#     - day   星期数，数字
#     - index 字符串，如 1-2，表示第一~二节课
#
from flask import Flask
from flask import request

with open('results.txt', 'r', encoding='utf-8') as f:
    items = [x.rstrip().split('\t') for x in f.readlines()]

items = items[1:]  # 去掉标题行
name_set = set([tuple(x[:3]) for x in items])  # 对姓名去重

# 用字典存  (周数， 周几, 节数) -> (有课的人)
course_map = dict()
for item in items:
    # 部门, 学号, 姓名, 日索引, 课程时间, 周索引
    _group, _id, _name, _day, _index, _week = tuple(item)
    key = (int(_week), int(_day), int(_index))
    val = (_group, _id, _name)
    if key not in course_map:
        course_map[key] = set()
        course_map[key].add(val)
    else:
        course_map[key].add(val)

# 启动服务器
app = Flask(__name__)


@app.route('/query', methods=['POST'])
def query():
    week = int(request.form['week'])
    day = int(request.form['day'])
    index = request.form['index']
    index = tuple(index.split('-'))

    # 查询
    coursed_member_set = set()
    for i in index:
        try:
            coursed_members = course_map[(week, day, int(i))]
        except KeyError:
            coursed_members = set()
        coursed_member_set = coursed_member_set.union(coursed_members)
    # 作差
    available_members = list(name_set - coursed_member_set)
    result = list(map(lambda person: {
        'group': person[0],
        'id': person[1],
        'name': person[2],
    }, available_members))

    return {'status': 200, 'result': result}, 200
