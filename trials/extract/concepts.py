# Concepts Collection
concepts_collection = db['Concepts']

# Function to insert concepts into MongoDB
def insert_concepts(file_path):
    with open(file_path, 'r') as f:
        publications_data = json.load(f)

    for publication in publications_data:
        for concept in publication.get('concepts', []):
            concept_record = {
                "_id": concept['id'],
                "name": concept['display_name'],
                "publications": [publication['id']]
            }
            concepts_collection.update_one(
                {"_id": concept_record["_id"]}, 
                {"$set": concept_record}, 
                upsert=True
            )
    print("Concepts successfully inserted into MongoDB.")

# Call the function after fetching data
insert_concepts('data/raw/openalex_data_20211014_103045.json')
