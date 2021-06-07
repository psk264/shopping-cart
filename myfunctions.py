import os
from dotenv import load_dotenv

load_dotenv()

def calculate_tax(subtotal):
    # print("Reading TAX RATE from env file..")
    # print(os.getenv("TAX_RATE"))
    tax = subtotal*float(os.getenv("TAX_RATE"))
    return tax


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71