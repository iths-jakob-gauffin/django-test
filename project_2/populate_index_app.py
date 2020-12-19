import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_2.settings')

import django
django.setup()

from faker import Faker
fakegen = Faker()

from index_app.models import User

def populate(N=5):
  for entry in range(N):
    fake_user = fakegen.profile(fields=['username'])['username']
    fake_first_name = fakegen.first_name()
    fake_last_name = fakegen.last_name()
    fake_email = fakegen.email()

    user = User.objects.get_or_create(user=fake_user, first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]
    user.save()

print("initializing population")
populate(10)
print('population complete')