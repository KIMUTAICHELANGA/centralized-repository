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
topics_collection = db['topics']

# Path to the processed data folder
data_folder = os.path.join('data', 'processed')

# Function to upload data from a specific subfolder to a MongoDB collection
def upload_data_from_subfolder(subfolder_name, collection):
    subfolder_path = os.path.join(data_folder, subfolder_name)
    
    if not os.path.exists(subfolder_path):
        print(f"Subfolder {subfolder_name} does not exist. Skipping.")
        return

    for filename in os.listdir(subfolder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(subfolder_path, filename)
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                    if isinstance(data, list):
                        collection.insert_many(data)
                    else:
                        collection.insert_one(data)
                    print(f"Data from {filename} uploaded to {subfolder_name} collection.")
                except json.JSONDecodeError as e:
                    print(f"Error reading {filename}: {e}")
                except Exception as e:
                    print(f"Error uploading {filename} to {subfolder_name} collection: {e}")

# Main function to upload data from all subfolders
def upload_all_data():
    upload_data_from_subfolder('publications', publications_collection)
    upload_data_from_subfolder('authors', authors_collection)
    upload_data_from_subfolder('institutions', institutions_collection)
    upload_data_from_subfolder('topics', topics_collection)

if __name__ == "__main__":
    upload_all_data()
    print("Data upload completed.")
