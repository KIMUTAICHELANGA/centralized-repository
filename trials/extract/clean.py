import os
import json
from datetime import datetime
from jsonschema import validate, ValidationError

# Create the processed directories if they don't exist
for folder in ['publications', 'authors', 'institutions', 'topics']:  # Change 'concepts' to 'topics'
    os.makedirs(f'data/processed/{folder}', exist_ok=True)

# Function to load raw data from respective folders
def load_raw_data(data_type):
    raw_folder = f'data/raw/{data_type}'
    # Get the latest JSON file from the folder
    files = [f for f in os.listdir(raw_folder) if f.endswith('.json')]
    if not files:
        raise FileNotFoundError(f"No raw data files found for {data_type}.")
    
    latest_file = max([os.path.join(raw_folder, f) for f in files], key=os.path.getctime)
    
    with open(latest_file, 'r') as f:
        return json.load(f)

# Clean and transform Publications
def clean_and_transform_publications(works):
    cleaned_data = []
    
    for work in works:
        publication_data = {
            "_id": work.get("id", "N/A"),
            "title": work.get("title", "N/A"),
            "abstract": work.get("abstract", "N/A"),
            "publication_date": work.get("publication_date", None),
            "authors": [author["author"]["display_name"] for author in work.get("authorships", [])],
            "doi": work.get("doi", "N/A"),
            "publisher": work.get("host_venue", {}).get("display_name", "N/A"),
            "url": work.get("id", "N/A"),
            "tags": [topics["display_name"] for topics in work.get("topics", [])],  # Change 'concepts' to 'topics'
            "related_topics": [topics["display_name"] for topics in work.get("topics", [])],  # Change 'concepts' to 'topics'
            "created_at": datetime.utcnow().isoformat()
        }
        cleaned_data.append(publication_data)

    return cleaned_data

# Clean and transform Authors
def clean_and_transform_authors(works):
    cleaned_data = []

    for work in works:
        for author in work.get("authorships", []):
            author_data = {
                "_id": author['author']['id'],
                "name": author['author']['display_name'],
                "orcid": author['author'].get('orcid', 'N/A'),
                "affiliation": [institution['display_name'] for institution in author.get('institutions', [])],
                "publications": [work.get("id", "N/A")],
                "created_at": datetime.utcnow().isoformat()
            }
            cleaned_data.append(author_data)

    return cleaned_data

# Clean and transform Institutions
def clean_and_transform_institutions(works):
    cleaned_data = []

    for work in works:
        for author in work.get("authorships", []):
            for institution in author.get('institutions', []):
                institution_data = {
                    "_id": institution['id'],
                    "name": institution['display_name'],
                    "country": institution.get('country', 'N/A'),
                    "publications": [work.get("id", "N/A")],
                    "created_at": datetime.utcnow().isoformat()
                }
                cleaned_data.append(institution_data)

    return cleaned_data

# Clean and transform Topics
def clean_and_transform_topics(works):
    cleaned_data = []

    for work in works:
        for topic in work.get("topics", []):  # Change 'concept' to 'topic'
            topic_data = {  # Change variable name from 'concept_data' to 'topic_data'
                "_id": topic['id'],  # Change variable from 'topics' to 'topic'
                "name": topic['display_name'],  # Change variable from 'topics' to 'topic'
                "publications": [work.get("id", "N/A")],
                "created_at": datetime.utcnow().isoformat()
            }
            cleaned_data.append(topic_data)  # Change variable from 'concept_data' to 'topic_data'

    return cleaned_data

# Load schema from the corresponding file
def load_schema(data_type):
    schema_file = f'data/schema/content_schema_{data_type}.json'
    with open(schema_file, 'r') as f:
        return json.load(f)

# Validate the cleaned data against the schema
def validate_data(data, schema):
    for item in data:
        try:
            validate(instance=item, schema=schema)
        except ValidationError as e:
            print(f"Validation error for item: {item}\nError: {e.message}")
            return False
    return True

# Save the processed data to respective folders
def save_processed_data(cleaned_data, data_type):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_path = f'data/processed/{data_type}/cleaned_data_{timestamp}.json'
    
    with open(file_path, 'w') as f:
        json.dump(cleaned_data, f, indent=4)
    
    print(f"Cleaned {data_type} data successfully saved to {file_path}")

# Main function to load, clean, validate, and save data
def process_data(data_type, clean_func):
    works = load_raw_data(data_type)  # Step 1: Load raw data
    cleaned_data = clean_func(works)  # Step 2: Clean data
    schema = load_schema(data_type)  # Load the schema for validation
    
    if validate_data(cleaned_data, schema):  # Validate the cleaned data
        save_processed_data(cleaned_data, data_type)  # Step 3: Save processed data if valid
    else:
        print(f"Data validation failed for {data_type}. Check the errors above.")

if __name__ == "__main__":
    # Process each data type with the respective cleaning function
    process_data('publications', clean_and_transform_publications)
    process_data('authors', clean_and_transform_authors)
    process_data('institutions', clean_and_transform_institutions)
    process_data('topics', clean_and_transform_topics)  # Change 'concepts' to 'topics'
