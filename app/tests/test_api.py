import unittest
import json
from flask import url_for

from app import create_app
from config import test


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        """
        Create app environment with test settings
        """

        self.app = create_app(test)
        self.client = self.app.test_client()
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()

    def test_(self):
        data = {'commands': '5 5'}
        resp = self.client.post(
                url_for('api.executeMovements'),
                data=json.dumps(data),
                content_type='application/json')
        self.assertEqual(resp.status_code, 200)
