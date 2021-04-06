from typing import List, Dict

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

    @staticmethod
    def _group_timetable(course_list: List[Course]) -> Dict[str, List[Course]]:
        result: Dict[str, List[Course]] = {}
        for course in course_list:
            course_name = course.course_name
            if course_name in result:
                result[course_name].append(course)
            else:
                result[course_name] = [course]

        return result

    def get_grouped_timetable(self, school_year: SchoolYear, semester: Semester) -> Dict[str, List[Course]]:
        time_table = self.get_timetable(school_year, semester)
        return self._group_timetable(time_table)

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
