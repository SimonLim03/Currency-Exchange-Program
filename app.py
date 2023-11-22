import streamlit as st
from datetime import datetime
from currency import CurrencyConverter
from checks import check_arguments, check_date

def main():
    st.title("Currency Exchange Converter")

    # Extract the input arguments
    args = st.text_input("Enter date, source currency, and target currency (separated by space):").split()

    if args and check_arguments(args):
        date_str, source_currency, target_currency = args

        # Check the validity of the input date
        if check_date(date_str):
            # Instantiate an object from the CurrencyConverter class with the verified currency codes and date
            converter = CurrencyConverter(source_currency.upper(), target_currency.upper(), date_str)

            # Check the validity of the currency codes
            if converter.check_currencies():
                amount = st.number_input("Enter the amount to be converted:", value=1.0)

                # Extract the historical rate and calculate its inverse rate
                rate, inverse_rate = converter.get_historical_rate(amt=amount)

                st.write("Conversion Result:")
                st.write(f"Amount: {amount} {source_currency}")
                st.write(f"Source Currency: {source_currency}")
                st.write(f"Converted Amount: {rate:.2f} {target_currency}")
                st.write(f"Target Currency: {target_currency}")
                st.write(f"Inverse Rate: {inverse_rate}")
            else:
                st.warning("Invalid currency codes. Please enter valid currency codes.")
        else:
            st.warning("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    else:
        st.warning("Invalid arguments. Please enter date, source currency, and target currency.")
    
if __name__ == "__main__":
    main()