
import sys
from frankfurter import Frankfurter

class CurrencyConverter:
    """
    Class that represents a Currency conversion object. It will be used to store the input arguments (currency codes, date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    api : Frankfurter
        Instance of Frankfurter class
    """
    def __init__(self, from_currency, to_currency, date):
        # => To be filled by student
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.currencies = f"https://api.frankfurter.app/latest?&{self.from_currency}&{self.to_currency}"
        self.base_url = "https://api.frankfurter.app/"
        self.date = date
        self.currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
        self.api = Frankfurter(self.base_url, self.currencies, self.currency_list)
        self.inverse_rate = 0
    def check_currencies(self):
        """
        Method that will check if currency codes stored in the class attributes are valid.
        Otherwise the program will exit and display the relevant message provided in the assignment brief

        Parameters
        ----------
        # => object

        Pseudo-code
        ----------
        # => checks if the currency exists by calling check currency from frankfurter class

        Returns
        -------
        # => TRUE if the currency exixts else exits
        """
        # => To be filled by student

        if self.api.check_currency(self.to_currency):
            if self.api.check_currency(self.from_currency):
                return True
            else:
                print(f"{self.from_currency} is not a valid currency code")
        else:
            print(f"{self.to_currency} is not a valid currency code")
        exit(0)

    def reverse_rate(self):
        """
        Method that will calculate the inverse rate from the value stored in the class attribute, round it to 4 decimal places and save it back in the class attribute inverse_rate.

        Parameters
        ----------
        # => The object 

        Pseudo-code
        ----------
        # => To be filled by student

        Returns
        -------
        # => reverse rate 
        """
        # => To be filled by student
        self.reverse_rate = self.round_rate(self.api.get_historical_rate(self.to_currency, self.from_currency, self.date))
        return self.reverse_rate
         

    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.

        Parameters
        ----------
        # => To be filled by student

        Pseudo-code
        ----------
        # => To be filled by student

        Returns
        -------
        # => To be filled by student
        """

        # => To be filled by student
        return round(float(rate), 4)

    def get_historical_rate(self, amt=1):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the assignment brief

        Parameters
        ----------
        # => To be filled by student

        Pseudo-code
        ----------
        # => To be filled by student

        Returns
        -------
        # => To be filled by student
        """

        # => To be filled by student
        rate =  self.round_rate(self.api.get_historical_rate(self.from_currency, self.to_currency,self.date, amount=amt))
        inverse_rate = self.round_rate(self.api.get_historical_rate(self.to_currency, self.from_currency,self.date, amount=amt))
        print(f"The conversion rate on {self.date} from {self.from_currency} to {self.to_currency} was {rate}. "
              f"The inverse rate is {inverse_rate}")
        return (rate, inverse_rate)