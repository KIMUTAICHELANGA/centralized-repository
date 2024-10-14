# Institutions Collection
institutions_collection = db['Institutions']

# Function to insert institutions into MongoDB
def insert_institutions(file_path):
    with open(file_path, 'r') as f:
        publications_data = json.load(f)

    for publication in publications_data:
        for author in publication.get('authorships', []):
            for institution in author.get('institutions', []):
                institution_record = {
                    "_id": institution['id'],
                    "name": institution['display_name'],
                    "country": institution.get('country_code', ''),
                    "publications": [publication['id']]
                }
                institutions_collection.update_one(
                    {"_id": institution_record["_id"]}, 
                    {"$set": institution_record}, 
                    upsert=True
                )
    print("Institutions successfully inserted into MongoDB.")

# Call the function after fetching data
insert_institutions('data/raw/openalex_data_20211014_103045.json')
