# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 13:39
# @Author  : sunnysab
# @File    : export-available-classrooms.py.py

import json


# See: src/parsers/timetable.py
__course_elements = [
    ('course_name', '课程名称', 'kcmc'),
    ('day', '星期', 'xqjmc'),
    ('time_index', '节次', 'jcs'),
    ('weeks', '周次', 'zcd'),
    ('place', '教室', 'cdmc'),
    ('teacher', '教师', 'xm'),
    ('campus', '校区', 'xqmc'),
    ('credit', '学分', 'xf'),
    ('hours', '学时', 'zxs'),
    ('dyn_class_id', '教学班', 'jxbmc'),
    ('course_id', '课程代码', 'kch'),
    ('prefered_class', '配课班', 'jxbzc'),
]
__cols = [x[0] for x in __course_elements]

# Load exported courses.
courses = json.load(open('courses.json', 'r', encoding='utf-8'))
processed_courses = []

# classroom -> { (week, day) -> flag }
classroom_mapping = dict()

for this_course in courses:
    # For readability, not for performance.
    processed_courses.append(this_course)

    classroom = this_course.get('place')
    if not classroom.startswith('一教') and not classroom.startswith('二教') and not classroom.startswith('南图')\
            and not classroom.startswith('32') and not classroom.startswith('34'):
        continue
    for i in this_course['time_index']:
        print(classroom)
        for w in this_course['weeks']:
            key = w * 10 + this_course['day']
            if classroom not in classroom_mapping:
                classroom_mapping[classroom] = dict()

            if key not in classroom_mapping[classroom]:
                classroom_mapping[classroom][key] = 2 ** i
            else:
                classroom_mapping[classroom][key] |= 2 ** i

# Write classrooms to file.
classrooms = sorted(classroom_mapping.keys())
open('classrooms_output.txt', 'w+', encoding='utf-8').writelines([x + '\n' for x in classrooms])

# Calculate available classroom time.
for classroom in classrooms:
    for week in range(1, 19):
        for day in range(1, 6):
            key = week * 10 + day
            if key not in classroom_mapping[classroom]:
                # Set flag = available all the day.
                classroom_mapping[classroom][key] = 0

# Write time table to file
with open('busy_time.txt', 'w+', encoding='utf-8') as out_file:
    for classroom in classrooms:
        for week_day in classroom_mapping[classroom]:
            out_file.write(
                f'{classroom}, {int(week_day / 10)}, {int(week_day % 10)}, {classroom_mapping[classroom][(week_day)]}\n')
# End of with clause
