import pandas as pd

def clean_gross_price(df):
    """Ensure that 'Gross Price' is exactly 2 decimal places."""
    df['Gross Price'] = df['Gross Price'].apply(lambda x: round(x, 2))
    return df

