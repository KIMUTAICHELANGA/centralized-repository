import os
import json
from datetime import datetime
from jsonschema import validate, ValidationError

# Create the processed directory if it doesn't exist
os.makedirs('data/processed', exist_ok=True)

# Load the raw data
def load_raw_data():
    raw_folder = 'data/raw'
    # Get the latest JSON file from the raw folder
    files = [f for f in os.listdir(raw_folder) if f.endswith('.json')]
    if not files:
        raise FileNotFoundError("No raw data files found.")
    latest_file = max([os.path.join(raw_folder, f) for f in files], key=os.path.getctime)
    
    with open(latest_file, 'r') as f:
        return json.load(f)

# Clean and transform data
def clean_and_transform_data(works):
    cleaned_data = []
    
    for work in works:
        content_data = {
            "title": work.get("title", "N/A"),
            "author": [author["author"]["display_name"] for author in work.get("authorships", [])],
            "published_date": work.get("publication_year", None),
            "content_type": work.get("type", "N/A"),
            "abstract": work.get("abstract", "N/A"),
            "image_url": work.get("image_url", None) if 'image_url' in work else None,
            "created_at": datetime.utcnow().isoformat()  # Add timestamp for processed data
        }
        cleaned_data.append(content_data)

    return cleaned_data

# Load schema
def load_schema():
    schema_file = 'data/schema/content_schema.json'
    with open(schema_file, 'r') as f:
        return json.load(f)

# Validate data against schema
def validate_data(data, schema):
    for item in data:
        try:
            validate(instance=item, schema=schema)
        except ValidationError as e:
            print(f"Validation error for item: {item}\nError: {e.message}")
            return False
    return True

# Save cleaned data to the processed folder
def save_processed_data(cleaned_data):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_path = f'data/processed/cleaned_data_{timestamp}.json'
    
    with open(file_path, 'w') as f:
        json.dump(cleaned_data, f, indent=4)
    
    print(f"Cleaned data successfully saved to {file_path}")

def main():
    works = load_raw_data()  # Step 1: Load raw data
    cleaned_data = clean_and_transform_data(works)  # Step 2: Clean data
    schema = load_schema()  # Load the schema for validation
    
    if validate_data(cleaned_data, schema):  # Validate the cleaned data
        save_processed_data(cleaned_data)  # Step 3: Save processed data if valid
    else:
        print("Data validation failed. Check the errors above.")

if __name__ == "__main__":
    main()
