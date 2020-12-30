from typing import List

import requests

from global_config import URL, REQUEST_OPTION
from parsers import *


class User:
    _user: str = None
    _session: requests.Session = None

    def __init__(self, user: str, session: requests.Session):
        self._user = user
        self._session = session

    def get_profile(self) -> Profile:
        page = self._session.get(URL.PROFILE, headers=REQUEST_OPTION)
        return parse_profile_page(page.text)

    def get_timetable(self, school_year: SchoolYear, semester: Semester) -> List[Course]:
        data = {
            'xnm': str(school_year),
            'xqm': semester.to_raw(),
        }
        page = self._session.post(URL.TIME_TABLE, data=data, headers=REQUEST_OPTION)
        return timetable.parse_timetable_page(page.text)

    def get_score_list(self, school_year: SchoolYear, semester: Semester) -> List[Score]:
        data = {
            'xnm': str(school_year),
            'xqm': semester.to_raw(),
            'queryModel.showCount': '5000',
        }
        page = self._session.post(URL.SCORE_LIST, data=data, headers=REQUEST_OPTION)
        return parse_score_list_page(page.text)

    @staticmethod
    def calculate_GPA(score_list: List[Score]) -> float:
        return calculate_GPA(score_list)

    def get_GPA(self, school_year: SchoolYear, semester: Semester):
        score_list = self.get_score_list(school_year, semester)
        return calculate_GPA(score_list)

# End of the class User.
