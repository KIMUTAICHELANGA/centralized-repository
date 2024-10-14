from pymongo import MongoClient
import json

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['openalex_db']
publications_collection = db['Publications']

# Function to insert publication data into MongoDB
def insert_publications(file_path):
    with open(file_path, 'r') as f:
        publications_data = json.load(f)
        
    for publication in publications_data:
        publication_record = {
            "_id": publication['id'],
            "title": publication.get('title', ''),
            "abstract": publication.get('abstract', ''),
            "publication_date": publication.get('publication_date', ''),
            "authors": [author['display_name'] for author in publication.get('authorships', [])],
            "doi": publication.get('doi', ''),
            "publisher": publication.get('host_venue', {}).get('display_name', ''),
            "url": publication.get('id', ''),
            "tags": publication.get('concepts', []),
            "related_concepts": [concept['display_name'] for concept in publication.get('concepts', [])]
        }
        
        publications_collection.insert_one(publication_record)
    print("Publications successfully inserted into MongoDB.")

# Call the function after fetching data
insert_publications('data/raw/openalex_data_20211014_103045.json')
