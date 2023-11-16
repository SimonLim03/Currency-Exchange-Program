# Currency Converter Using Python

## Author
Name: Simon Lim

## Description
This application is a currency converter, which allows to quickly convert one currency to another currency.
This project used an open-source API: https://www.frankfurter.app/.
The goal of the program is to display the current conversion rate between 2 currency codes at a specific date. It will also calculate the inverse conversion rate between these 2 currencies.

## How to Run the Program
To run this application, a specific inputs in the console should be typed.
python main.py <year-month-date> <currency1> <currency2>
For example, it can be:
python main.py 2002-01-01 GBP AUD
Once its processed, the following output will show up.
"Enter the amount to be converted"
and once the specific amount is typed, 
the outputs about conversion rate from currency 1 to currency 2 and inversion rate will show up.

## Project Structure
<p>
api.py: This file contains the code for making API calls.
</p>

<p>
checks.py: This python file contains codes for checking date and input arguments. 
</p>

<p>
currency.py: This python file contains class that is used to store input arguments and other information and as well as calculating inverse rate, round rate and historical rate.
</p>

<p>
frankfurter.py: This python file contains the class used for calling relevant Frankfurter endpoints, including base url, historical url and currencies url.
</p>

<p>
main.py: This file contains main functioning for running the codes in other files. 
</p>

<p>
test_api.py: python script for testing codes from api.py
</p>

<p>
test_checks.py: python script for testing codes from check.py
</p>

<p>
test_currency.py: python script for testing codes from currency.py
</p>

<p>
test_frankfurter.py: python script for testing codes from frankfurter.py
</p>

