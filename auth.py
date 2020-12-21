import base64
import json
import re
import rsa
import requests

from global_config import URL, REQUEST_OPTION
from typing import Tuple

session = requests.Session()


def create_session() -> requests.Session:
    return requests.Session()


def encrypt_in_rsa(message: bytes, public_key: bytes, exponent: bytes) -> str:
    public_key: int = int.from_bytes(public_key, byteorder='big')
    exponent: int = int.from_bytes(exponent, byteorder='big')

    crypted_passwd: bytes = rsa.encrypt(message, rsa.PublicKey(n=public_key, e=exponent))
    return base64.b64encode(crypted_passwd).decode('utf-8')


class Session:
    user: str = None
    passwd: str = None
    session: requests.Session = None

    def __init__(self, user: str = None, passwd: str = None):
        self.user = user
        self.passwd = passwd

    def get_ras_public_key(self) -> Tuple[bytes, bytes]:
        resp_obj = self.session.get(URL.RSA_PUBLIC_KEY, headers=REQUEST_OPTION).json()
        return base64.b64decode(resp_obj['modulus']), base64.b64decode(resp_obj['exponent'])

    def get_csrf_token(self, login_page: str) -> str:
        token_tag = re.compile(r'<input type="hidden" id="csrftoken" name="csrftoken" value="(.*)"/>')
        return token_tag.search(login_page).group(1)

    def get_err_message(self, content: str) -> str:
        from bs4 import BeautifulSoup

        page = BeautifulSoup(content, 'html5lib')
        err_node = page.select(r'div#home.tab-pane.in.active p#tips.bg_danger.sl_danger')[0]
        return err_node.text.strip()

    def login(self, user: str = user, passwd: str = passwd) -> Tuple[bool, str]:
        self.session = requests.Session()

        # Get login page for the first cookie
        login_page = session.get(URL.LOGIN, headers=REQUEST_OPTION)

        # Get RAS public key to encode the raw password
        public_key, exponent = self.get_ras_public_key()
        encrypted_passwd: str = encrypt_in_rsa(passwd.encode('utf-8'), public_key, exponent)

        form_to_post = {
            'csrftoken': self.get_csrf_token(login_page.text),
            'language': 'zh_CN',
            'yhm': user,
            'mm': encrypted_passwd
        }
        r = self.session.post(URL.LOGIN, data=form_to_post, allow_redirects=False)
        if r.status_code == 302:
            return True, ''
        else:
            return False, self.get_err_message(r.text)
