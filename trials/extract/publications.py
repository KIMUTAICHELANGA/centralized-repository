import os
import json
import requests

# Create the necessary directories for storing raw data
os.makedirs('data/raw/publications', exist_ok=True)

# Function to fetch publications from OpenAlex API
def fetch_publications(limit=10):
    url = "https://api.openalex.org/works"
    params = {
        "page": 1,
        "per_page": limit
    }
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
    os.makedirs(f'data/raw/{folder_name}', exist_ok=True)
    
    # Save data as rawpublications.json
    file_path = f'data/raw/{folder_name}/rawpublications.json'
    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"Publications data saved in {file_path}")

# Main function to extract and save publications
def main():
    publications = fetch_publications(limit=10)
    save_data(publications, 'publications')

if __name__ == "__main__":
    main()
