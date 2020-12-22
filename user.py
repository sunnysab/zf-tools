from typing import List

import requests

import parsers.profile as profile
import parsers.score as scores
import parsers.timetable as timetable
from global_config import URL
from parsers.defines import SchoolYear, Semester


class User:
    _user: str = None
    _session: requests.Session = None

    def __init__(self, user: str, session: requests.Session):
        self._user = user
        self._session = session

    def get_profile(self) -> profile.Profile:
        page = self._session.get(URL.PROFILE)
        return profile.parse_profile_page(page.text)

    def get_timetable(self, school_year: SchoolYear, semester: Semester) -> List[timetable.Course]:
        data = {
            'xnm': str(school_year),
            'xqm': semester.to_raw(),
        }
        page = self._session.post(URL.TIME_TABLE, data=data)
        return timetable.parse_timetable_page(page.text)

    def get_score_list(self, school_year: SchoolYear, semester: Semester) -> List[scores.Score]:
        data = {
            'xnm': str(school_year),
            'xqm': semester.to_raw(),
            'queryModel.showCount': '5000',
        }
        page = self._session.post(URL.SCORE_LIST, data=data)
        return scores.parse_score_list_page(page.text)

    @staticmethod
    def calculate_GPA(score_list: List[scores.Score]) -> float:
        return scores.calculate_GPA(score_list)

    def get_GPA(self, school_year: int, semester: Semester):
        score_list = self.get_score_list(school_year, semester)
        return scores.calculate_GPA(score_list)

# End of the class User.
