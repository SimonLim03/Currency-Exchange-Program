import unittest
from frankfurter import Frankfurter

class TestUrl(unittest.TestCase):
    """
    Class used for testing the url attributes of the Frankfurter class from checks.py
    """
    
    def test_check_frankfurter_class(self):
        currencies = f"https://api.frankfurter.app/latest?&EUR&USD"
        base_url = "https://api.frankfurter.app/"
        currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF',
                         'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON',
                         'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
        obj = Frankfurter(base_url, currencies, currency_list)
        if obj.base_url and obj.currencies_url and obj.currencies:
            assert True
        else:
            assert False


class TestCurrenciesList(unittest.TestCase):
    """
    Class used for testing the currencies attribute of the Frankfurter class from checks.py
    """
  
    def test_currency_list(self):
        currencies = f"https://api.frankfurter.app/latest?&EUR&USD"
        base_url = "https://api.frankfurter.app/"
        currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF',
                         'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON',
                         'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
        obj = Frankfurter(base_url, currencies, currency_list)
        assert isinstance(obj.get_currencies_list(), list)



class TestCheckCurrency(unittest.TestCase):
    """
    Class used for testing the Frankfurter.check_currency() method from frankfurter.py
    """
   
    def test_check(self):
        currencies = f"https://api.frankfurter.app/latest?&EUR&USD"
        base_url = "https://api.frankfurter.app/"
        currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF',
                         'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON',
                         'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
        obj = Frankfurter(base_url, currencies, currency_list)
        assert isinstance(obj.get_currencies_list(), list)


class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the Frankfurter.get_historical_rate() method from frankfurter.py
    """
   
    def test_check_historical(self):
        currencies = f"https://api.frankfurter.app/latest?&EUR&USD"
        base_url = "https://api.frankfurter.app/"
        currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF',
                         'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON',
                         'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
        obj = Frankfurter(base_url, currencies, currency_list)
        assert obj.get_historical_rate("EUR", "USD", "2020-01-01", 10) == 11.234

if __name__ == '__main__':
    unittest.main()
