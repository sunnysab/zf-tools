from src import session
from src.parsers import *

# s = session.Session()
# err_message = s.login('account', 'password')

s = session.SsoSession('account', 'password')
err_message = s.login()

if err_message == 'success':
    user = s.user()

    # env = s.environment()
    # c = env.get_suggested_course(SchoolYear(2020), Semester.SECOND_TERM, 'B2203', '20122311')
    # print(c)

    # time_table = user.get_grouped_timetable(SchoolYear(2020), Semester.SECOND_TERM)
    # for course_name in time_table:
    #     print(course_name)
    #     for each_class in time_table[course_name]:
    #         print(each_class)

    # scores = user.get_score_list(SchoolYear(), Semester.ALL)
    # for each_course_score in scores:
    #     print(each_course_score)
    # print(user.get_GPA(AllSchoolYear(), Semester.ALL))

    # env = s.environment()
    # majors = env.get_major_list(SchoolYear(2018))
    # for each_major in majors:
    #     print(each_major)
    #
    env = s.user()

    classes = env.get_timetable(SchoolYear(2020), Semester.SECOND_TERM)
    print(classes)

else:
    print(err_message)
