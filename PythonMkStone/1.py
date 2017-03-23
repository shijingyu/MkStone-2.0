from django.contrib import auth

user = auth.authenticate(username='sdsdssd', password='asdasd')
if user is not None:
    print 'true'
else:
    print 'false'