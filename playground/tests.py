from unittest import TestCase
from django.test import Client
import json

class TestApi_get_playground(TestCase):

    def setUp(self):
        self.client = Client()

    def test_api_get_blog_playground(self):
        data = {
            "jsonrpc": "2.0",
            "id":1,
            "method": "playground.get_blog"
        }
        response = self.client.post('/api/',json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)






