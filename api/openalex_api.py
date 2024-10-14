# openalex_api.py
import requests
from config import config

class OpenAlexAPI:
    def __init__(self):
        self.base_url = config['api']['openalex']['base_url']
        self.api_key = config['api']['openalex']['api_key']
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

    def fetch_data(self, endpoint, params=None):
        """
        Fetch data from OpenAlex API.

        :param endpoint: The specific endpoint to fetch data from.
        :param params: Optional query parameters for the request.
        :return: JSON response from the OpenAlex API or None if an error occurs.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response as JSON
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from OpenAlex: {e}")
            return None

    def get_single_entity(self, entity_id):
        """
        Fetch a single entity by its ID from the OpenAlex API.

        :param entity_id: The ID of the entity to fetch.
        :return: JSON response for the entity or None if an error occurs.
        """
        return self.fetch_data(f'works/{entity_id}')

    def get_list_of_entities(self, query):
        """
        Fetch a list of entities based on a query.

        :param query: The query string to search for entities.
        :return: JSON response with the list of entities or None if an error occurs.
        """
        params = {'q': query}
        return self.fetch_data('works', params=params)

    def get_group_of_entities(self, group_id):
        """
        Fetch a group of entities based on a group ID.

        :param group_id: The ID of the group to fetch.
        :return: JSON response for the group of entities or None if an error occurs.
        """
        return self.fetch_data(f'groups/{group_id}')

if __name__ == "__main__":
    openalex_api = OpenAlexAPI()

    # Example: Fetch a single entity by ID
    single_entity = openalex_api.get_single_entity("W12345678")  # Replace with actual ID
    print(single_entity)

    # Example: Fetch a list of entities based on a search query
    list_of_entities = openalex_api.get_list_of_entities("machine learning")
    print(list_of_entities)

    # Example: Fetch a group of entities
    group_of_entities = openalex_api.get_group_of_entities("group_id")  # Replace with actual group ID
    print(group_of_entities)
