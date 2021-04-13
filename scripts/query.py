# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 21:49
# @Author  : sunnysab
# @File    : query.py

with open('导出2.txt', 'r', encoding='utf-8') as f:
    items = [x.rstrip().split('\t') for x in f.readlines()]

# 去掉标题行
items = items[1:]

# 对姓名去重
name_set = set([tuple(x[:3]) for x in items])

# 用字典存  (周数， 周几, 节数) -> (有课的人)
course_map = dict()
for item in items:
    _group, _id, _name, _day, _index, _week = tuple(item)
    key = (_week, _day, _index)
    val = (_group, _id, _name)
    if key not in course_map:
        course_map[key] = set()
        course_map[key].add(val)
    else:
        course_map[key].add(val)

# 输入参数
week = input('第几周: ')
day = input('周几: ')
index = input('第几节课(如1-2): ')
index = tuple(index.split('-'))

# 查询
coursed_member_set = set()
for i in index:
    coursed_member_set = coursed_member_set.union(course_map[(week, day, i)])

# 作差
v = name_set - coursed_member_set
for _v in v:
    print(_v)
