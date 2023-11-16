import unittest
from api import call_get
import requests

class TestAPI(unittest.TestCase):
    """
    Class used for testing the call_get() function in api.py
    """

    def test_call_get(self):
        currencies_url = f"https://api.frankfurter.app/latest?&EUR&USD"
        # self.base_url = "https://api.frankfurter.app/"
        resp = call_get(currencies_url)
        assert isinstance(resp, requests.models.Response)

    def test_call_get_negative(self):
        currencies_url = f"https://api.frankfurter22.app/latest?&EUR&USD121"
        # self.base_url = "https://api.frankfurter.app/"
        resp = call_get(currencies_url)

        assert resp is None

if __name__ == '__main__':
    unittest.main()

