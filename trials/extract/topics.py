import os
import json
import requests

# Create the necessary directories for storing raw data
os.makedirs('/data/raw/topics', exist_ok=True)

# Function to fetch topics from OpenAlex API, grouped by field.id
def fetch_topics_grouped_by_field(limit=10):
    url = "https://api.openalex.org/topics"
    params = {
        "group_by": "field.id",  # Group by field.id
        "page": 1,
        "per_page": limit
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'mailto': 'briankimu97@gmail.com'
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    
    return response.json()['group_by']  # Return grouped results

# Function to save data to the specified folder
def save_data(data, folder_name):
    # Ensure the folder exists
    os.makedirs(f'/data/raw/{folder_name}', exist_ok=True)

    # Save data as rawtopics.json
    file_path = f'/data/raw/{folder_name}/rawtopics_grouped_by_field.json'

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Grouped topics data saved in {file_path}")

# Main function to extract and save grouped topics
def main():
    topics_grouped_by_field = fetch_topics_grouped_by_field(limit=10)
    save_data(topics_grouped_by_field, 'topics')

if __name__ == "__main__":
    main()
