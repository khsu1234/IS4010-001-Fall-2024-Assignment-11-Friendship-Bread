import pandas as pd

def identify_and_save_anomalies(df, output_path):
    """Identify rows where 'Fuel Type' is 'Pepsi' and save them to a new CSV."""
    anomalies = df[df['Fuel Type'].str.lower() == 'pepsi']
    anomalies.to_csv(output_path, index=False)
    # Drop rows with "Pepsi" from the original DataFrame
    df = df[df['Fuel Type'].str.lower() != 'pepsi']
    return df

