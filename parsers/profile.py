from collections import namedtuple
from bs4 import BeautifulSoup


__elements = [
    ('student_no', '学号', '#col_xh > p:nth-child(1)'),
    ('name', '姓名', '#col_xm > p:nth-child(1)'),
    ('name_eng', '英文姓名', '#col_ywxm > p:nth-child(1)'),
    ('sex', '性别', '#col_xbm > p:nth-child(1)'),
    ('credential_type', '证件类型', '#col_zjlxm > p:nth-child(1)'),
    ('credential_id', '证件号码', '#col_zjhm > p:nth-child(1)'),
    ('birth_date', '出生日期', '#col_csrq > p:nth-child(1)'),
    ('ethnicity', '民族', '#col_mzm > p:nth-child(1)'),
    ('hometown', '籍贯', '#col_jg > p:nth-child(1)'),
    ('enrollment_date', '入学日期', '#col_rxrq > p:nth-child(1)'),
    ('type', '学生类型', '#col_xslxdm > p:nth-child(1)')
]

Profile = namedtuple('Profile', [x for x, _, _ in __elements])


def get_profile_url(user: str):
    return f'http://jwxt.sit.edu.cn/jwglxt/xsxxxggl/xsgrxxwh_cxXsgrxx.html?gnmkdm=N100801&layout=default&su=#{user}'


def parse_profile_page(text: str) -> Profile:
    page = BeautifulSoup(text, 'html5lib')
    profile_fields = {}
    for field, _, selector in __elements:
        try:
            value = page.select(selector)[0].text.strip()
        except:
            value = ''
        profile_fields[field] = value

    return Profile(**profile_fields)


if __name__ == '__main__':
    content = open('profile.html', 'r', encoding='utf-8').read()
    profile = parse_profile_page(content)
    print(profile)
