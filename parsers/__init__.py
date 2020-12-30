# -*- coding: utf-8 -*-
# @Time    : 2020/12/30 16:32
# @Author  : sunnysab
# @File    : __init__.py

""" Namedtuple """
from .defines import SchoolYear, AllSchoolYear, Semester
from .classes import Major, Class
from .user_profile import Profile
from .score import Score
from .timetable import Course

""" Method """
from .classes import parse_major_list_page, parse_class_list_page
from .user_profile import parse_profile_page
from .score import parse_score_list_page, calculate_GPA
from .timetable import parse_timetable_page

# End of file
