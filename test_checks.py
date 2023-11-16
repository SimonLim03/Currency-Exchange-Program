import unittest
from checks import check_arguments, check_date


class TestCheckArguments(unittest.TestCase):
    """
    Class used for testing the check_arguments() function from checks.py
    """
    # => To be filled by student
    def test_check_arguments(self):
        assert check_arguments(["EUR", "USD", "1/1/2020"])

    def test_check_arguments_negative(self):
        assert not check_arguments(["EUR", "1/1/2020"])

class TestCheckDate(unittest.TestCase):
    """
    Class used for testing the check_date() function from checks.py
    """
    # => To be filled by student
    def test_check_date(self):
        assert check_date("2020-09-09")
    def test_check_date_negative(self):
        assert not check_date("2020-09/09")

if __name__ == '__main__':
    unittest.main()