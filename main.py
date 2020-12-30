import session
from parsers import *

s = session.Session()
err_message = s.login('user', 'password')

if err_message == 'success':
    pass

    user = s.user()
    scores = user.get_score_list(SchoolYear(), Semester.ALL)
    for each_course_score in scores:
        print(each_course_score)
    print(user.get_GPA(AllSchoolYear(), Semester.ALL))

    env = s.environment()
    majors = env.get_major_list(SchoolYear(2018))
    for each_major in majors:
        print(each_major)

    classes = env.get_class_list(SchoolYear(2018), Semester.SECOND_TERM)
    for each_class in classes:
        print(each_class)

else:
    print(err_message)
