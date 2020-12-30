# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 9:40
# @Author  : sunnysab
# @File    : environment.py


import requests
from global_config import URL, REQUEST_OPTION
from parsers import *


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

    def get_class_list(self, school_year: SchoolYear, semester: Semester):
        data = {
            'xnm': str(school_year),
            'xqm': semester.to_raw(),
            'queryModel.showCount': 10000,
        }
        page = self._session.post(URL.CLASS_LIST, data=data, headers=REQUEST_OPTION)
        return parse_class_list_page(page.text)
