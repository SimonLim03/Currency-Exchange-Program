import unittest
from currency import CurrencyConverter

class TestCurrencyConverterInstantiation(unittest.TestCase):
    """
    Class used for testing the instanciation of the CurrencyConverter class from currency.py
    """
    
    def test_currency_convertor_instantiation(self):
        obj = CurrencyConverter("EUR", "USD", "2020-01-01")
        if obj.to_currency and obj.from_currency:
            assert True
        else:
            assert False

class TestCurrencyCheck(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.check_currencies() method from currency.py
    """
    def test_currency_check(self):
        assert CurrencyConverter("EUR", "USD", "2020-01-01").check_currencies()

class TestReverseRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.reverse_rate() method from currency.py
    """
    
    def test_currency_check(self):
        assert isinstance(CurrencyConverter("EUR", "USD", "2020-01-01").reverse_rate(), float)
    
class TestRoundRate(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.round_rate() method from currency.py
    """
   
    def test_round_rate(self):
        num = CurrencyConverter("EUR", "USD", "2020-01-01").round_rate("127.4321232")
        assert 4 == len(str(num).split(".")[1])

class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.get_historical_rate() method from currency.py
    """
    
    def test_check_rate(self):
        num = CurrencyConverter("EUR", "USD", "2020-01-01").get_historical_rate(10)
        assert len(num) == 2
    
if __name__ == '__main__':
    unittest.main()
