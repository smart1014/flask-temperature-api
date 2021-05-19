import unittest
import json

from main import app


class TestTemperatureAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def get_api_response(self, p_type, p_value):
        payloads = json.dumps({
            "type": p_type,
            "value": p_value
        })
        response = self.app.post(
            '/api/v1/converter',
            headers={"Content-Type": "application/json"},
            data=payloads
        )
        return response

    def test_wrong_params(self):
        response = self.get_api_response("d", 32)
        self.assertEqual(200, response.status_code)
        self.assertEqual("Validation Error", response.json)

    def test_fahrenheit_to_celcius(self):
        response = self.get_api_response("f", 61.7)
        self.assertEqual(200, response.status_code)
        self.assertEqual("16.50", response.json)

    def test_celcius_to_fahrenheit(self):
        response = self.get_api_response("c", 23)
        self.assertEqual(200, response.status_code)
        self.assertEqual("73.40", response.json)

    def test_zero_fahrenheit(self):
        response = self.get_api_response("f", 0)
        self.assertEqual(200, response.status_code)
        self.assertEqual("-17.78", response.json)

    def test_zero_celcius(self):
        response = self.get_api_response("c", 0)
        self.assertEqual(200, response.status_code)
        self.assertEqual("32.00", response.json)