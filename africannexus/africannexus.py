import requests
import os
import json

# Set up the directory for saving raw data
os.makedirs('data/raw', exist_ok=True)

# Replace with your African Nexus API endpoint and any necessary credentials
BASE_URL = 'https://api.africannexus.org'  # African Nexus API base URL
ENDPOINT = '/data'  # Update with the actual endpoint you want to access
API_KEY = 'your_api_key'  # Replace with your actual API key if needed

# Function to get data from African Nexus
def get_african_nexus_data(endpoint, api_key):
    url = f"{BASE_URL}{endpoint}"
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def save_raw_data(data, filename):
    with open(f'data/raw/{filename}', 'w') as f:
        json.dump(data, f)

def main():
    raw_data = get_african_nexus_data(ENDPOINT, API_KEY)
    
    if raw_data:
        # Save the raw JSON data
        save_raw_data(raw_data, 'african_nexus_data.json')
        print("African Nexus data saved successfully.")

if __name__ == "__main__":
    main()
