# mongodb_connection.py
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError
import logging
import os
from dotenv import load_dotenv  # New import for environment variables

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MongoDBConnection:
    def __init__(self, uri=None, database_name=None):
        """
        Initialize the MongoDB connection.

        :param uri: MongoDB URI (including credentials if needed).
        :param database_name: Name of the database to connect to.
        """
        self.uri = uri or os.getenv("MONGODB_URI")
        self.database_name = database_name or os.getenv("MONGODB_DATABASE")
        self.client = None
        self.database = None

    def connect(self):
        """Connect to the MongoDB database."""
        try:
            logger.info("Connecting to MongoDB...")
            self.client = MongoClient(self.uri)
            self.database = self.client[self.database_name]
            logger.info("Successfully connected to MongoDB.")
        except ConnectionFailure as e:
            logger.error("Failed to connect to MongoDB: %s", e)
        except ConfigurationError as e:
            logger.error("Configuration error: %s", e)

    def insert_to_mongodb(self, collection_name, data):
        """
        Insert data into a specified MongoDB collection.

        :param collection_name: Name of the collection where data will be inserted.
        :param data: Data to be inserted (should be a dictionary).
        """
        if not self.database:
            logger.error("Not connected to the database.")
            return

        try:
            collection = self.database[collection_name]
            if isinstance(data, list):
                result = collection.insert_many(data)
                logger.info(f"Inserted {len(result.inserted_ids)} documents into {collection_name}.")
            else:
                result = collection.insert_one(data)
                logger.info(f"Inserted document with ID: {result.inserted_id} into {collection_name}.")
        except Exception as e:
            logger.error("Error inserting data into MongoDB: %s", e)

    def close(self):
        """Close the MongoDB connection."""
        if self.client:
            self.client.close()
            logger.info("MongoDB connection closed.")

if __name__ == "__main__":
    load_dotenv()  # Load environment variables
    mongo_connection = MongoDBConnection(database_name=os.getenv("MONGODB_DATABASE"))
    mongo_connection.connect()

    # Example data to insert
    example_data = {
        "title": "Sample Document",
        "authors": ["Author One", "Author Two"],
        "publication_date": "2023-10-14",
        "source": "Example Source"
    }

    mongo_connection.insert_to_mongodb('your_collection_name', example_data)

    # Close the connection when done
    mongo_connection.close()
