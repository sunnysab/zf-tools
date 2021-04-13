# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 17:22
# @Author  : sunnysab
# @File    : export-course.py

from typing import List, Tuple
import src as zf

"""
    加载 group.csv，每行为逗号分隔的 [部门、姓名、学号、密码]
"""
# [(user, password), ...]
preprocess = lambda line: tuple(line.rstrip().split('\t'))

with open('group.csv', 'r', encoding='utf-8') as f:
    members: List[Tuple[str, str, str, str]] = list(map(preprocess, f.readlines()))
print(f'加载了 {len(members)} 个账户.')

"""
    登录，然后读课表
"""
output = open('results.txt', 'w+', encoding='utf-8')

for group, name, stu_num, passwd in members:
    session = zf.SsoSession(stu_num, passwd)

    try:
        session.login()
        u = session.user()
    except Exception as e:
        print(f'{group} {name}({stu_num}) 登录失败: {str(e)}')
        continue

    time_table = u.get_timetable(zf.SchoolYear(2020), zf.Semester.SECOND_TERM)
    for course in time_table:
        for index in course.time_index:
            for week in course.weeks:
                output.write(f'{group}\t{stu_num}\t{name}\t{course.day}\t{index}\t{week}\n')
    output.flush()
