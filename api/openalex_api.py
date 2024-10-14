# openalex_api.py
import requests
from config import config

def fetch_openalex_data(endpoint, params=None):
    """
    Fetch data from OpenAlex API.

    :param endpoint: The specific endpoint to fetch data from.
    :param params: Optional query parameters for the request.
    :return: JSON response from the OpenAlex API.
    """
    url = f"{config['api']['openalex']['base_url']}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {config['api']['openalex']['api_key']}"
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from OpenAlex: {e}")
        return None
