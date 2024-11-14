# Connect to django shell and run this script to populate the database with users
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userportal.settings')

import django
django.setup()

# FAKE POP SCRIPT
import random
from users.models import User
from faker import Faker

fakegeb = Faker()

def populate(N=5):
    for entry in range(N):
        # create the fake data for that entry
        fake_first_name = fakegeb.first_name()
        fake_last_name = fakegeb.last_name()
        fake_email = fakegeb.email()
        
        # create the new User entry
        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populating complete!")