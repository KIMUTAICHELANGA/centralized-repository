from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['openalex']  # Database name

# Define collections
publications_collection = db['publications']
authors_collection = db['authors']
institutions_collection = db['institutions']
concepts_collection = db['concepts']

# Sample documents for each collection
sample_publication = {
    "title": "Sample Publication Title",
    "abstract": "This is a sample abstract for the publication.",
    "publication_date": "2023-01-01",
    "authors": [],  # This will hold ObjectIds of authors
    "doi": "10.1234/sample.doi",
    "publisher": "Sample Publisher",
    "url": "http://example.com/sample-publication",
    "tags": ["sample", "publication"],
    "related_concepts": []  # This will hold ObjectIds of concepts
}

sample_author = {
    "name": "John Doe",
    "orcid": "0000-0001-2345-6789",
    "affiliation": [],  # This will hold ObjectIds of institutions
    "publications": []  # This will hold ObjectIds of publications
}

sample_institution = {
    "name": "Sample Institution",
    "country": "Sample Country",
    "publications": []  # This will hold ObjectIds of publications
}

sample_concept = {
    "name": "Sample Concept",
    "publications": []  # This will hold ObjectIds of publications
}

# Create collections and insert sample documents
publications_collection.insert_one(sample_publication)
authors_collection.insert_one(sample_author)
institutions_collection.insert_one(sample_institution)
concepts_collection.insert_one(sample_concept)

print("Database and collections created with sample documents.")
