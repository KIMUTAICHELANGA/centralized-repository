# orcid_api.py
import requests
from config import config

def fetch_orcid_data(endpoint, params=None):
    """
    Fetch data from ORCID API.

    :param endpoint: The specific endpoint to fetch data from.
    :param params: Optional query parameters for the request.
    :return: JSON response from the ORCID API.
    """
    url = f"{config['api']['orcid']['base_url']}{endpoint}"
    headers = {
        "Authorization": f"Bearer {config['api']['orcid']['api_key']}",
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from ORCID: {e}")
        return None
