# Authors Collection
authors_collection = db['Authors']

# Function to insert authors into MongoDB
def insert_authors(file_path):
    with open(file_path, 'r') as f:
        publications_data = json.load(f)

    for publication in publications_data:
        for author in publication.get('authorships', []):
            author_record = {
                "_id": author['author']['id'],
                "name": author['author']['display_name'],
                "orcid": author['author'].get('orcid', ''),
                "affiliation": [aff['display_name'] for aff in author.get('institutions', [])],
                "publications": [publication['id']]
            }
            authors_collection.update_one(
                {"_id": author_record["_id"]}, 
                {"$set": author_record}, 
                upsert=True
            )
    print("Authors successfully inserted into MongoDB.")

# Call the function after fetching data
insert_authors('data/raw/openalex_data_20211014_103045.json')
