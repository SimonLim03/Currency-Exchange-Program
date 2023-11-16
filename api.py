import requests
import sys

def call_get(url: str) -> requests.models.Response:
    """
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    In case of an error, the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    # => URL: string

    Pseudo-code
    ----------
    # => To be filled by student

    Returns
    -------
    # => response object
    """
    
    # => To be filled by student

    try:
        return requests.get(url=url)
    except Exception:
        print("Wrong endpoint")
        return None
