import auth
import user
from parsers.defines import SchoolYear, AllSchoolYear, Semester

s = auth.Session()
u = s.login('user', 'password')

if type(u) is user.User:
    scores = u.get_score_list(SchoolYear(), Semester.ALL)
    for s in scores:
        print(s)
    print(u.get_GPA(AllSchoolYear(), Semester.ALL))
else:
    print(u)
