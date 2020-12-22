import json
from collections import namedtuple
from typing import List

from parsers.defines import Semester

__elements = [
    ('score', '成绩', 'cj'),
    ('course', '课程', 'kcmc'),
    ('course_id', '课程代码', 'kch'),
    ('class_id', '班级', 'jxb_id'),
    ('school_year', '学年', 'xnmmc'),
    ('semester', '学期', 'xqm'),
    ('credit', '学分', 'xf'),
]

# New namedtuple type
Score = namedtuple('Score', [x for x, _, _ in __elements])


def parse_score_list_page(page: str) -> List[Score]:
    json_page = json.loads(page)
    course_list = json_page['items']
    result = []

    for course in course_list:
        fields = {}

        for field_name, _, raw_name in __elements:
            fields[field_name] = course[raw_name]

        '''
            Soem more processes.
        '''
        fields['score'] = float(fields['score'])
        fields['credit'] = float(fields['credit'])
        fields['semester'] = Semester.from_raw(fields['semester'])
        result.append(Score(**fields))

    return result


def calculate_GPA(scores: List[Score]):
    total_credits = 0.0
    t = 0.0

    for s in scores:
        # Some warnings happens for missing '.credit' or '.score' in class 'tuple' in Pycharm,
        # but they can be ignored.
        t += s.credit * s.score
        total_credits += s.credit

    return (t / total_credits / 10) - 5.0


if __name__ == '__main__':
    p = parse_score_list_page(open('score_list.json', 'r', encoding='utf-8').read())

    print(calculate_GPA(p))
