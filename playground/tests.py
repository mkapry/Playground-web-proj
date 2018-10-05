from django.test import TestCase, Client
import json
from django.contrib.auth.models import User
from playground.models import Blog


class TestEntryList(TestCase):
    def setUp(self):
        self.client=Client()
        #aself.user=User.objects.create(username='test_user',  email='test_user')
        self.blog=Blog.objects.create(name='test_blog')
        self.response_map={
            'name': 'test_blog',
        }



# Create your tests here.
