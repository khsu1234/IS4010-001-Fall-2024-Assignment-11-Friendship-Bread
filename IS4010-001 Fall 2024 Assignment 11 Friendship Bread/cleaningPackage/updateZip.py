import pandas as pd
import requests
import re

def extract_city(address):
    """Extract the city name from the address using a regular expression."""
    # Assuming the format includes "City, State ZIP" or similar.
    match = re.search(r'([a-zA-Z\s]+),\s+[A-Z]{2}', address)
    if match:
        return match.group(1).strip()
    return None

def get_zipcode_for_city(city, api_key):
    """Look up a valid zip code for a given city using the external API."""
    url = f'https://app.zipcodebase.com/api/v1/code/city'
    params = {
        'apikey': api_key,
        'city': city,
        'country': 'US'
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        # Get the first zip code from the response
        if 'results' in data and data['results']:
            zip_codes = list(data['results'].values())[0]
            return zip_codes[0] if zip_codes else None
    else:
        print(f"Error fetching zip code for {city}: {response.status_code}")
    return None

def update_missing_zip_codes(df, api_key):
    """Update missing zip codes in the DataFrame by looking up valid ones based on city name."""
    for index, row in df.iterrows():
        address = row['Full Address']
        if pd.isna(row.get('Zip Code')):  # Check if 'Zip Code' is missing
            city = extract_city(address)
            if city:
                zip_code = get_zipcode_for_city(city, api_key)
                if zip_code:
                    print(f"Adding zip code {zip_code} for city {city}")
                    df.at[index, 'Zip Code'] = zip_code
    return df