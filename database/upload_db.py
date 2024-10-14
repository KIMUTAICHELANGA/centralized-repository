import os
import json
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['openalex']  # Database name

# Collections
publications_collection = db['publications']
authors_collection = db['authors']
institutions_collection = db['institutions']
concepts_collection = db['concepts']

# Path to the data folder
data_folder = os.path.join('data', 'processed')  # Updated path to include 'processed' subfolder

# Function to upload data from JSON files
def upload_data():
    for filename in os.listdir(data_folder):
        if filename.endswith('.json'):
            with open(os.path.join(data_folder, filename), 'r') as file:
                data = json.load(file)
                
                # Determine which collection to use based on filename
                if filename.startswith('publications'):
                    publications_collection.insert_many(data)
                elif filename.startswith('authors'):
                    authors_collection.insert_many(data)
                elif filename.startswith('institutions'):
                    institutions_collection.insert_many(data)
                elif filename.startswith('concepts'):
                    concepts_collection.insert_many(data)
                else:
                    print(f"Unknown data type in file: {filename}")

if __name__ == "__main__":
    upload_data()
    print("Data upload completed.")
