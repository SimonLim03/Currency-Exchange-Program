from api import call_get

class Frankfurter:
    """
    Class that manages API calls to Frankfurter. It will be used to store the URLS to the relevant endpoints. It will also automatically call the Currencies endpoint and store the return list of available currency codes.

    Attributes
    ----------
    base_url : str
        Base url to Frankfurter API
    currencies_url : str
        Frankfurter endpoint for extracting currencies list
    historical_url : str
        Frankfurter endpoint for extracting historical currencies conversion rates
    currencies: list
        List of available currency codes
    """
    def __init__(self, base_url, currencies_url, currencies):

        # => To be filled by student
        self.base_url = base_url
        self.currencies_url = currencies_url
        #self.historical_url = historical_url
        self.currencies = currencies

    def get_currencies_list(self):
        """
        Method that will get the list of available currencies and returns it as a Python list.

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
        return self.currencies

    def check_currency(self, currency):
        """
        Method that will check if a provided currency code is valid and return True if that is the case.
        Otherwise it will return False.

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
        if currency in self.currencies:
            return True
        return False

    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
        """
        Method that will call the historical API endpoint in order to get the conversion rate for a given dates and currencies. It will return an requests.models.Response object.

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
        url = f"{self.base_url}{from_date}?from={from_currency}&to={to_currency}&amount={amount}"
        #print(url)
        response = call_get(url)
        amount =response.json()['rates'][to_currency]
        return amount
