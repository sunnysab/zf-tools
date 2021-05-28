# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 17:22
# @Author  : sunnysab
# @File    : export-course.py

from typing import List, Tuple

import src as zf

"""
    加载 group.csv，每行为 TAB 分隔的 [部门、姓名、学号、密码]
    用 TAB 分隔列是因为有些人的密码中含半角逗号
    注意：在 PyCharm 中打开 csv 文件并按下 TAB 时，IDE 可能会将 TAB 自动转换成若干空格，所以清确认你实际输入的字符
"""
# [(user, password), ...]
strip_split = lambda line: tuple(line.rstrip().split('\t'))

with open('group.csv', 'r', encoding='utf-8') as f:
    members: List[Tuple[str, str, str, str]] = list(map(strip_split, f.readlines()))
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
