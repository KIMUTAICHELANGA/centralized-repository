from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['openalex']  # Database name

# Define collections
publications_collection = db['publications']
authors_collection = db['authors']
institutions_collection = db['institutions']
concepts_collection = db['concepts']

# Sample documents for each collection matching the schema

# Sample publication document
sample_publication = {
    "_id": "pub_123456",  # Unique identifier for the publication
    "title": "Sample Publication Title",
    "abstract": "This is a sample abstract for the publication.",
    "publication_date": "2023-01-01",  # ISO 8601 formatted date (YYYY-MM-DD)
    "authors": [],  # This will hold ObjectIds of authors (should be updated with actual ObjectIds)
    "doi": "10.1234/sample.doi",
    "publisher": "Sample Publisher",
    "url": "http://example.com/sample-publication",
    "tags": ["sample", "publication"],
    "related_concepts": [],  # This will hold ObjectIds of related concepts
    "created_at": datetime.utcnow().isoformat()  # Ensure this field matches schema requirement
}

# Sample author document
sample_author = {
    "_id": "auth_789012",  # Unique identifier for the author
    "name": "John Doe",
    "orcid": "0000-0001-2345-6789",  # Optional ORCID field
    "affiliation": [],  # This will hold ObjectIds of institutions (should be updated with actual ObjectIds)
    "publications": [],  # This will hold ObjectIds of related publications
    "created_at": datetime.utcnow().isoformat()  # Ensure created_at is in ISO format
}

# Sample institution document
sample_institution = {
    "_id": "inst_345678",  # Unique identifier for the institution
    "name": "Sample Institution",
    "country": "Sample Country",  # Country name or null if unknown
    "publications": [],  # This will hold ObjectIds of related publications
    "created_at": datetime.utcnow().isoformat()  # Ensure created_at is in ISO format
}

# Sample concept document
sample_concept = {
    "_id": "concept_901234",  # Unique identifier for the concept
    "name": "Sample Concept",
    "publications": [],  # This will hold ObjectIds of related publications
    "created_at": datetime.utcnow().isoformat()  # Ensure created_at is in ISO format
}

# Insert sample documents into respective collections
publications_id = publications_collection.insert_one(sample_publication).inserted_id
authors_id = authors_collection.insert_one(sample_author).inserted_id
institutions_id = institutions_collection.insert_one(sample_institution).inserted_id
concepts_id = concepts_collection.insert_one(sample_concept).inserted_id

# Print confirmation
print(f"Sample documents inserted with IDs:\nPublication ID: {publications_id}\nAuthor ID: {authors_id}\nInstitution ID: {institutions_id}\nConcept ID: {concepts_id}")
