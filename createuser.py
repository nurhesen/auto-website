from django.contrib.auth.models import User

try:
    usr=User.objects.create_superuser('test', 'test@example.com', 'test')

except:
    pass