import json
from collections import namedtuple
from typing import List

__elements = [
    ('course_name', '课程名称', 'kcmc'),
    ('day', '星期', 'xqjmc'),
    ('time_index', '节次', 'jcs'),
    ('weeks', '周次', 'zcd'),
    ('place', '教室', 'cdmc'),
    ('teacher', '教师', 'xm'),
    ('campus', '校区', 'xqmc'),
    ('credit', '学分', 'xf'),
    ('hours', '学时', 'zxs'),
    ('dyn_class_id', '教学班', 'jxbmc'),
    ('course_id', '课程代码', 'kch'),
    ('prefered_class', '配课班', 'jxbzc'),
]

# New namedtuple type
Course = namedtuple('Course', [x for x, _, _ in __elements])


# Day map
DAY_MAP = {
    '星期一': 1,
    '星期二': 2,
    '星期三': 3,
    '星期四': 4,
    '星期五': 5,
    '星期六': 6,
    '星期日': 7,
}


def __expand_weeks_str(week_string: str) -> tuple:
    """
    Expand weeks' str to a tuple of weeks.
    For example: We gets a string '1-6周(单)', so the function returns a tuple of (1, 3, 5)
    Last but not least, multi-section-string like '1-9周,11-12周,14周' is supported.
    :return: A tuple that indicates the weeks.
    """
    if ',' in week_string:  # Call self recursively
        weeks = []
        for x in week_string.split(','):
            weeks.extend(__expand_weeks_str(x))
    else:
        step = 2 if week_string.endswith('(单)') or week_string.endswith('(双)') else 1
        try:
            start, end = week_string[:week_string.index('周')].split('-')
            weeks = list(range(int(start), int(end) + 1, step))
        except ValueError:
            # ValueError is going to be thrown when week_string may be like '3周'
            weeks = week_string[:week_string.index('周')]
            weeks = [int(weeks)]

    return tuple(weeks)


def __expand_time_index(time_string: str) -> tuple:
    """
    Expand time string like '1-2' to a tuple of indices.
    :return: a tuple of indices
    """
    try:
        start, end = time_string.split('-')
        indices = list(range(int(start), int(end) + 1))
    except ValueError:
        # ValueError is going to be thrown when week_string may be like '1'
        indices = [int(time_string)]
    return tuple(indices)


def parse_timetable_page(page: str) -> List[Course]:
    json_page = json.loads(page)
    course_list = json_page['kbList']
    result = []

    for course in course_list:
        fields = {}

        for field_name, _, raw_name in __elements:
            item = course.get(raw_name, '')
            fields[field_name] = item

        """
            Some more processes
        """
        # '1-3周,5周' -> (1, 2, 3, 5)
        fields['weeks'] = __expand_weeks_str(fields['weeks'])
        # '1-3' -> (1, 2, 3)
        fields['time_index'] = __expand_time_index(fields['time_index'])
        # '赵,钱,孙,李' -> ['赵','钱','孙','李']
        fields['teacher'] = tuple(fields['teacher'].split(','))
        # '星期一' -> 1
        fields['day'] = DAY_MAP[fields['day']]
        # '20108311;20108312' -> ['20108311', '20108312']
        fields['prefered_class'] = tuple(fields['prefered_class'].split(';'))
        # '1.5' -> 1.5
        fields['credit'] = float(fields['credit'])
        fields['hours'] = float(fields['credit'])
        fields['dyn_class_id'] = fields['dyn_class_id'].strip() if fields['dyn_class_id'] is not None else None

        result.append(Course(**fields))

    return result


if __name__ == '__main__':
    content = json.load(open('timetable.json', 'r', encoding='utf-8'))
    print(parse_timetable_page(content))
