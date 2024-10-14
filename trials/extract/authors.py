import os
import json
import requests
from datetime import datetime

# Create the necessary directories for storing raw data
os.makedirs('data/raw/authors', exist_ok=True)

# Function to fetch authors from OpenAlex API with a filter
def fetch_authors(filters=None, limit=10):
    url = "https://api.openalex.org/authors"
    params = {
        "page": 1,
        "per_page": limit
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
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_path = f'data/raw/{folder_name}/data_{timestamp}.json'
    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"Authors data saved in {file_path}")

# Main function to extract and save authors
def main():
    authors_filters = "has_orcid:true"  # Example filter for authors
    authors = fetch_authors(filters=authors_filters, limit=10)
    save_data(authors, 'authors')

if __name__ == "__main__":
    main()
