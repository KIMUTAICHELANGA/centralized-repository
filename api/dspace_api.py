# dspace_api.py
import requests
from config import config

def fetch_dspace_data(endpoint, params=None):
    """
    Fetch data from DSpace API.

    :param endpoint: The specific endpoint to fetch data from.
    :param params: Optional query parameters for the request.
    :return: JSON response from the DSpace API.
    """
    url = f"{config['api']['dspace']['base_url']}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {config['api']['dspace']['api_key']}"
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from DSpace: {e}")
        return None
