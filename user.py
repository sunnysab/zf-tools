import requests
from typing import List
import parsers.profile as profile
import parsers.timetable as timetable


class User:
    _user: str = None
    _session: requests.Session = None

    def __init__(self, user: str, session: requests.Session):
        self._user = user
        self._session = session

    def get_profile(self) -> profile.Profile:
        page = self._session.get(profile.get_profile_url(self._user))
        return profile.parse_profile_page(page.text)

    def get_timetable(self, school_year: int, semester: timetable.Semester) -> List[timetable.Course]:
        data = {
            'xnm': school_year,
            'xqm': semester.to_raw(),
        }
        page = self._session.post(timetable.get_timetable_url(self._user), data=data)
        return timetable.parse_timetable_page(page.text)
