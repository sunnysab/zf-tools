# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 9:20
# @Author  : sunnysab
# @File    : select_course.py

import json
from collections import namedtuple
from typing import List

__elements = [
    ('course_name', '课程名称', 'kzmc'),
    ('sub_course_name', '实际课程名称', 'kcmc'),
    ('course_id', '课程代码', 'kch'),
    ('college', '开课学院', 'kklxdm'),  # 开课学院代码
    ('total_size', '课程人数', 'yxzrs'),  # 已选择人数
    ('inner_dyn_class_id', '课程序号(内部表示)', 'jxb_id'),
    ('dyn_class_id', '课程序号', 'jxbmc'),
]

# New namedtuple type
Course = namedtuple('Course', [x for x, _, _ in __elements])


def parse_available_course_page(page: str) -> List[Course]:
    json_page = json.loads(page)
    result = []

    for course in json_page:
        fields = {}

        for field_name, _, raw_name in __elements:
            fields[field_name] = course[raw_name]

        result.append(Course(**fields))

    return result
