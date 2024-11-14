import pandas as pd
from cleaningPackage.deleteDupe import remove_duplicates
from cleaningPackage.deletePepsi import identify_and_save_anomalies
from cleaningPackage.twoDecimal import clean_gross_price
from cleaningPackage.updateZip import update_missing_zip_codes

def main():
    # File paths
    input_file_path = 'Data/fuelPurchaseData.csv'
    output_cleaned_data_path = 'Data/cleanedData.csv'
    output_anomalies_path = 'Data/dataAnomalies.csv'
    
    # Load the CSV file
    df = pd.read_csv(input_file_path, low_memory=False)
    
    # Step 1: Clean Gross Price to 2 decimal places
    df = clean_gross_price(df)
    
    # Step 2: Remove duplicate rows
    df = remove_duplicates(df)
    
    # Step 3: Identify and save anomalies (rows with "Pepsi" in the Fuel Type)
    df = identify_and_save_anomalies(df, output_anomalies_path)
    
    # Step 4: Update missing zip codes based on city
    api_key = '14c91670-a28b-11ef-baef-8bbb9bae37b5'
    df = update_missing_zip_codes(df, api_key)
    
    # Step 5: Save the cleaned data
    df.to_csv(output_cleaned_data_path, index=False)

if __name__ == "__main__":
    main()
