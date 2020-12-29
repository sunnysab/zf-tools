import session
from parsers.defines import SchoolYear, AllSchoolYear, Semester

s = session.Session()
err_message = s.login('user', 'password')

if err_message == 'success':
    user = s.user()
    scores = user.get_score_list(SchoolYear(), Semester.ALL)
    for each_course_score in scores:
        print(each_course_score)
    print(user.get_GPA(AllSchoolYear(), Semester.ALL))

else:
    print(err_message)
