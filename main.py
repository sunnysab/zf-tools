import auth
import user

s = auth.Session()
u = s.login('user', 'password')

if type(u) is user.User:
    print(u.get_profile())
else:
    print(u)