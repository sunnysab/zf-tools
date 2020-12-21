import auth

u = auth.Session()

print(u.login('user', 'password'))