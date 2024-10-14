import requests
import os

# Set up the directory for saving raw data
os.makedirs('data/raw', exist_ok=True)

# Replace with your ORCID API endpoint and any necessary credentials
BASE_URL = 'https://pub.orcid.org/v3.0'  # ORCID API base URL
ORCID_ID = 'your_orcid_id'  # Replace with your actual ORCID ID

# Function to get data from ORCID
def get_orcid_data(orcid_id):
    url = f"{BASE_URL}/{orcid_id}/works"
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def save_raw_data(data, filename):
    with open(f'data/raw/{filename}', 'w') as f:
        f.write(data)

def main():
    raw_data = get_orcid_data(ORCID_ID)
    
    if raw_data:
        # Save the raw JSON data
        save_raw_data(json.dumps(raw_data), 'orcid_data.json')
        print("ORCID data saved successfully.")

if __name__ == "__main__":
    main()
