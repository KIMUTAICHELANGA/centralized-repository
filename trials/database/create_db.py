from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime, timezone

# Connection URI (make sure to replace <db_password> with your actual password)
uri = "mongodb+srv://briankimu97:oRdjnfn3xNy8xcGw@cluster0.zbx2b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    db = client['openalex']  # Database name

    # Define collections
    publications_collection = db['publications']
    authors_collection = db['authors']
    institutions_collection = db['institutions']
    topics_collection = db['topics']

    # Sample documents for each collection matching the schema
    sample_publication = {
        "_id": "pub_123456",
        "title": "Sample Publication Title",
        "abstract": "This is a sample abstract for the publication.",
        "publication_date": "2023-01-01",
        "authors": [],
        "doi": "10.1234/sample.doi",
        "publisher": "Sample Publisher",
        "url": "http://example.com/sample-publication",
        "tags": ["sample", "publication"],
        "related_concepts": [],
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    sample_author = {
        "_id": "auth_789012",
        "name": "John Doe",
        "orcid": "0000-0001-2345-6789",
        "affiliation": [],
        "publications": [],
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    sample_institution = {
        "_id": "inst_345678",
        "name": "Sample Institution",
        "country": "Sample Country",
        "publications": [],
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    sample_topics = {
        "_id": "concept_901234",
        "name": "Sample Topics",
        "publications": [],
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    # Insert sample documents into respective collections
    publications_id = publications_collection.insert_one(sample_publication).inserted_id
    authors_id = authors_collection.insert_one(sample_author).inserted_id
    institutions_id = institutions_collection.insert_one(sample_institution).inserted_id
    topics_id = topics_collection.insert_one(sample_topics).inserted_id

    # Print confirmation
    print(f"Sample documents inserted with IDs:\nPublication ID: {publications_id}\nAuthor ID: {authors_id}\nInstitution ID: {institutions_id}\nTopics ID: {topics_id}")

except Exception as e:
    print("An error occurred:", e)
