import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create the raw directory if it doesn't exist
os.makedirs('data/raw', exist_ok=True)

# Function to fetch data from OpenAlex API with search functionality
def fetch_openalex_data(search_term=None, limit=10, search_field=None):
    url = "https://api.openalex.org/works"
    
    # Basic params for research outputs, limiting the number of results
    params = {
        "page": 1,
        "per_page": limit  # Limit the number of results fetched
    }
    
    # Add search term with field filtering if specified
    if search_field and search_term:
        params[f"{search_field}.search"] = search_term
    elif search_term:
        params["search"] = search_term  # General search for titles, abstracts, and full text

    # Include your email in the headers for identification
    headers = {
        'User-Agent': 'your_user_agent_string',  # Customize this string as needed
        'mailto': 'briankimu97@gmail.com'  # Add your email here
    }

    # Make the API request
    response = requests.get(url, params=params, headers=headers)
    
    # Raise an error for bad responses
    response.raise_for_status()

    # Save data to the raw folder
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_path = f'data/raw/openalex_data_{timestamp}.json'
    
    with open(file_path, 'w') as f:
        json.dump(response.json()['results'], f, indent=4)
    
    print(f"Data successfully fetched and stored in {file_path}")

if __name__ == "__main__":
    # Example usage: Fetch works with a specific term, limiting to 10 results
    fetch_openalex_data(search_term="dna", limit=10)  # General search
    # fetch_openalex_data(search_term="cubist", limit=10, search_field="title")  # Field-specific search
