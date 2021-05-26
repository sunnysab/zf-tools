# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 12:56
# @Author  : sunnysab
# @File    : export-suggested-course.py

import json

from src import *

s = Session('account', 'password')
err_message = s.login()

if err_message != 'success':
    print('Login failed: ', err_message)
    exit(-1)

env = s.environment()

""" Step 1 """
# Get all majors
classes = env.get_class_list(SchoolYear(2020), Semester.SECOND_TERM)
# Filter classes. Note: some majors have 5 years' study.
classes = [x for x in classes if x.grade in [2016, 2017, 2018, 2019, 2020]]

""" Step 2 """
# Fetch suggested_course for all classes.
courses = []
loaded_count = 0
for c in classes:
    suggested_course = env.get_suggested_course(SchoolYear(2020), Semester.SECOND_TERM, c.major_id, c.class_id, c.grade)
    courses.extend(suggested_course)

    loaded_count += 1
    if loaded_count % 10 == 0:
        print(f'{loaded_count} classes are loaded, total {len(courses)} results by now.')
        # time.sleep(5)

json.dump(courses, open('courses.json', 'w+', encoding='utf-8'))
