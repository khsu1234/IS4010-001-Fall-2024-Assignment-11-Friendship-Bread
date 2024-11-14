import pandas as pd

def remove_duplicates(df):
    """Remove duplicate rows."""
    return df.drop_duplicates()

