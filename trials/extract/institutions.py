import os
import json
import requests
from datetime import datetime

# Create the necessary directories for storing raw data
os.makedirs('/data/raw/institutions', exist_ok=True)  # Ensure the path is correct

# Function to fetch institutions from OpenAlex API with a filter and grouping
def fetch_institutions(filters=None, limit=10):
    url = "https://api.openalex.org/institutions"
    params = {
        "page": 1,
        "per_page": limit,
        "group_by": "continent"  # Group by continent
    }
    
    if filters:
        params['filter'] = filters

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'mailto': 'briankimu97@gmail.com'
    }
    
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    
    return response.json()['results']

# Function to save data to the specified folder
def save_data(data, folder_name):
    # Create the directory if it doesn't exist
    os.makedirs(f'/data/raw/{folder_name}', exist_ok=True)
    
    # Save data as rawinstitutions.json
    file_path = f'/data/raw/{folder_name}/rawinstitutions.json'
    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"{folder_name.capitalize()} data saved in {file_path}")

# Main function to extract and save institutions
def main():
    institutions_filters = "country_code:ca"  # Example filter for institutions in Canada
    institutions = fetch_institutions(filters=institutions_filters, limit=10)
    save_data(institutions, 'institutions')

if __name__ == "__main__":
    main()
