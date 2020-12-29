# -*- coding: utf-8 -*-
# @Time    : 2020-12-29 9:14
# @Author  : sunnysab
# @File    : classes.py

import json
from collections import namedtuple
from typing import List

__elements_major = [
    ('entrance_year', '入学年份', 'njdm'),
    ('id', '专业代码', 'zyh'),
    ('name', '专业名称', 'zymc'),
    ('inner_id', '专业内部标识', 'zyh_id'),
    ('direction_id', '专业方向内部表示', 'zyfx_id'),
    ('direction', '专业方向', 'zyfxmc'),
]

__elements_class = [
    ('grade', '年级', 'njmc'),
    ('college', '学院', 'jgmc'),
    ('major_name', '专业名称', 'zymc'),
    ('major_id', '专业代码', 'zyh_id'),
    ('class_id', '班级', 'bh'),
]

# New namedtuple type
Major = namedtuple('Major', [x for x, _, _ in __elements_major])
Class = namedtuple('Class', [x for x, _, _ in __elements_class])


def parse_major_list_page(page: str) -> List[Major]:
    json_page = json.loads(page)
    result = []

    for major in json_page:
        fields = {}
        for field_name, _, raw_name in __elements_major:
            fields[field_name] = major[raw_name]

        # Some more process
        fields['entrance_year'] = int(fields['entrance_year'])

        result.append(Major(**fields))

    return result


def parse_class_list_page(page: str) -> List[Class]:
    json_page = json.loads(page)
    result = []
    i = 0

    while i < len(json_page):
        fields = {}
        _class = json_page[i]

        for field_name, _, raw_name in __elements_class:
            fields[field_name] = _class.get(raw_name, None)

        # Some more process
        fields['grade'] = int(fields['grade'])

        result.append(Class(**fields))
        i += 1

    return result
