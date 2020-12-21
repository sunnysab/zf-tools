import requests
import parsers.profile as profile

from global_config import URL

class User:
    _user: str = None
    _passwd: str = None
    _session: requests.Session = None

    def __init__(self, user: str, session: requests.Session):
        self._user = user
        self._session = session

    def get_profile(self) -> profile.Profile:
        page = self._session.get(profile.get_profile_url(self._user))
        return profile.parse_profile_page(page.text)
