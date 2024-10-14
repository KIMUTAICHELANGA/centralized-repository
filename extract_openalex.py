import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('OPENALEX_API_KEY')

# Create the raw directory if it doesn't exist
os.makedirs('data/raw', exist_ok=True)

# Function to fetch data from OpenAlex API with search functionality
def fetch_openalex_data(search_term=None, limit=10):
    url = "https://api.openalex.org/works"
    
    # Basic params for research outputs, limiting the number of results
    params = {
        "filter": "is_research_output:true",
        "page": 1,
        "per_page": limit  # Limit the number of results fetched
    }
    
    # Add search term if provided
    if search_term:
        params["search"] = search_term

    # Include the API key in the headers if required
    headers = {
        'Authorization': f'Bearer {API_KEY}' if API_KEY else None
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    # Save data to the raw folder
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_path = f'data/raw/openalex_data_{timestamp}.json'
    
    with open(file_path, 'w') as f:
        json.dump(response.json()['results'], f, indent=4)
    
    print(f"Data successfully fetched and stored in {file_path}")

if __name__ == "__main__":
    # Example usage: Fetch works with a specific term, limiting to 10 results
    fetch_openalex_data(search_term="dna", limit=10)
