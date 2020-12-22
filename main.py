import auth
import user
from parsers.defines import Semester

s = auth.Session()
u = s.login('user', 'password')

if type(u) is user.User:
    scores = u.get_score_list(2019, Semester.SECOND_TERM)
    print(scores)
    print(u.get_GPA(2019, Semester.SECOND_TERM))
else:
    print(u)
