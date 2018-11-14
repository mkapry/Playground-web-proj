from unittest import TestCase
from django.test import Client
import json
from core.models import User
from django.test.utils import override_settings
class TestApi_get_playground(TestCase):

    def setUp(self):
        self.client = Client()
        print(User.objects.all())
        user = User()
        user.username="mkapry"
        user.save()
        print(User.objects.all())
        self.id_author = user.id

    def test_api_get_blog_playground(self):
        data = {
            "jsonrpc": "2.0",
            "id":1,
            "method": "playground.get_blog"
        }
        response = self.client.post('/api/', json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        expected = {'id': 1, 'jsonrpc': '2.0', 'result': []}
        self.assertEqual( expected, response.json() )


    def test_api_add_blog_playground(self):
        #self.client.post('/login', {'user': 'mkapry', 'password': 'smith'})

        data = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "playground.get_blog",
        }
        response = self.client.post('/api/', json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        expected = {'id': 1, 'jsonrpc': '2.0', 'result': []}
        self.assertEqual(expected, response.json())

        data = {
            "jsonrpc": "2.0",
            "id":1,
            "method": "playground.add_blog",
            "params": {"user": "mkapry", "name": "sport", "author": self.id_author}
        }
        response = self.client.post('/api/', json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)

        data = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "playground.get_blog",
        }
        response = self.client.post('/api/', json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        expected = {'id': 1,
                      'jsonrpc': '2.0',
                      'result': [{'fields': {'author': 1,
                                             'name': 'sport',
                                             'model': 'playground.blog',
                                             'pk': 1}}]}
        print( expected )
        print( response.json() )
        self.assertEqual(expected, response.json())



