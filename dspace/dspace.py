import requests
import os
import json

# Set up the directory for saving raw data
os.makedirs('data/raw', exist_ok=True)

# Replace with your DSpace API endpoint and any necessary credentials
BASE_URL = 'http://your-dspace-instance/api'  # Update with your DSpace API URL
ENDPOINT = '/core/items'  # Update with the actual endpoint you want to access
USERNAME = 'your_username'  # Your DSpace username
PASSWORD = 'your_password'  # Your DSpace password

# Function to get data from DSpace
def get_dspace_data(endpoint, username, password):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, auth=(username, password), headers={'Accept': 'application/json'})

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
    raw_data = get_dspace_data(ENDPOINT, USERNAME, PASSWORD)
    
    if raw_data:
        # Save the raw JSON data
        save_raw_data(raw_data, 'dspace_data.json')
        print("DSpace data saved successfully.")

if __name__ == "__main__":
    main()
