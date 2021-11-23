# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 9:40
# @Author  : sunnysab
# @File    : environment.py


from typing import List

import requests

from .global_config import URL, REQUEST_OPTION, COOKIE_DICT
from .parsers import *


class Environment:
    _session: requests.Session = None

    def __init__(self, session: requests.Session):
        self._session = session

    def get_major_list(self, entrance_year: SchoolYear) -> Major:
        param = {
            'njdm_id': str(entrance_year),
        }
        page = self._session.get(URL.MAJOR_LIST, params=param, headers=REQUEST_OPTION)
        return parse_major_list_page(page.text)

    def get_class_list(self, school_year: SchoolYear, semester: Semester) -> List[Class]:
        data = {
            'xnm': str(school_year),
            'xqm': semester.to_raw(),
            'queryModel.showCount': 10000,
        }
        page = self._session.post(URL.CLASS_LIST, data=data, headers=REQUEST_OPTION, cookies=COOKIE_DICT)
        return parse_class_list_page(page.text)

    def get_suggested_course_list(self, school_year: SchoolYear, semester: Semester, major_id: str, class_id: str,
                                  class_new_id: str, entrance_year: str = None) -> List[Course]:
        if not entrance_year:
            entrance_year = '20' + class_id[:2]
        data = {
            'xnm': str(school_year),
            'xqm': semester.to_raw(),
            'njdm_id': entrance_year,
            'zyh_id': major_id,
            'bh_id': class_new_id,
            # The two are unknown but necessary :-(
            'tjkbzdm': '1',
            'tjkbzxsdm': '0',
        }
        page = self._session.post(URL.SUGGESTED_COURSE, data=data, headers=REQUEST_OPTION, cookies=COOKIE_DICT)
        return parse_timetable_page(page.text)
