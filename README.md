# Currency Converter Using Python

## Author
Name: Simon Lim
Student ID: 24661225

## Description
This application is a currency converter, which allows to quickly convert one currency to another currency.
First, I struggled making input arguments and other information to be stored in currency class. 
Furthermore, codings about historical rates in currency class and historical API endpoints were not easy and took many times to complete. 
Fortunately, instructions really helped me how to establish codes for each method. 


## How to Setup
It starts with creating main.py and then making codes for functions of check_argument and check_date with possible errors. 
And then started working with currency class, which involves storing input arguments and other information and as well as methods of check currency, 
reverse rate, round rate and historical rate. Furthermore, API calls regarding check currency and historical rate methods are managed in frankfurther class. Frankfurther class is used to store URLS to the relevant endpoints.
Finally, api class use requests to call API endpoint and return URL. 
Python version is 3.9.13


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
api.py: This file contains the code for making API calls.
checks.py: This python file contains codes for checking date and input arguments. 
currency.py: This python file contains class that is used to store input arguments and other information and as well as calculating inverse rate, round rate and historical rate.
frankfurter.py: This python file contains the class used for calling relevant Frankfurter endpoints, including base url, historical url and currencies url.
main.py: This file contains main functioning for running the codes in other files. 
test_api.py: python script for testing codes from api.py
test_checks.py: python script for testing codes from check.py
test_currency.py: python script for testing codes from currency.py
test_frankfurter.py: python script for testing codes from frankfurter.py


## Citations

