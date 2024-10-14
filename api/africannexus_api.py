# africannexus_api.py
import requests
from config import config

def fetch_africannexus_data(endpoint, params=None):
    """
    Fetch data from African Nexus API.

    :param endpoint: The specific endpoint to fetch data from.
    :param params: Optional query parameters for the request.
    :return: JSON response from the African Nexus API.
    """
    url = f"{config['api']['africannexus']['base_url']}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {config['api']['africannexus']['api_key']}"
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from African Nexus: {e}")
        return None
