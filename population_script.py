import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

# Fake Script
import random
from start_app.models import Topic, Access, Webpage, User
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.free_email()
        webpg =  Webpage.objects.get_or_create(topic = top, url=fake_url, name=fake_name)[0]

        access_rec = Access.objects.get_or_create(name=webpg, date=fake_date)

        user_details =  User.objects.get_or_create(first_name = fake_fname, last_name =fake_lname, email=fake_email)[0]


if __name__ == '__main__':
    print("Populating Script!")
    populate(20)
    print("Populating Complete!")