import unittest
from unittest.mock import patch, MagicMock
from pymongo.errors import ConnectionFailure
from mongodb_connection import MongoDBConnection


class TestMongoDBConnection(unittest.TestCase):
    
    @patch('mongodb_connection.MongoClient')
    def setUp(self, mock_mongo_client):
        """Set up the MongoDBConnection object for testing."""
        self.mongo_uri = 'mongodb://testuser:testpass@localhost:27017/testdb'
        self.db_name = 'testdb'
        self.mongo_connection = MongoDBConnection(uri=self.mongo_uri, database_name=self.db_name)
        self.mongo_connection.connect()

    @patch('mongodb_connection.MongoClient')
    def test_connect_success(self, mock_mongo_client):
        """Test successful connection to MongoDB."""
        mock_mongo_client.return_value.__getitem__.return_value = MagicMock()
        self.mongo_connection.connect()
        self.assertIsNotNone(self.mongo_connection.client)
        self.assertEqual(self.mongo_connection.database_name, self.db_name)

    @patch('mongodb_connection.MongoClient')
    def test_connect_failure(self, mock_mongo_client):
        """Test connection failure."""
        mock_mongo_client.side_effect = ConnectionFailure("Connection failed")
        with self.assertLogs('mongodb_connection', level='ERROR') as log:
            self.mongo_connection.connect()
            self.assertIn('ERROR:mongodb_connection:Failed to connect to MongoDB: Connection failed', log.output)

    @patch('mongodb_connection.MongoClient')
    def test_insert_one_success(self, mock_mongo_client):
        """Test inserting a single document."""
        mock_collection = MagicMock()
        mock_collection.insert_one.return_value.inserted_id = "12345"
        mock_mongo_client.return_value.__getitem__.return_value = mock_collection
        
        self.mongo_connection.insert_to_mongodb('test_collection', {"key": "value"})
        mock_collection.insert_one.assert_called_once()
        
    @patch('mongodb_connection.MongoClient')
    def test_insert_many_success(self, mock_mongo_client):
        """Test inserting multiple documents."""
        mock_collection = MagicMock()
        mock_collection.insert_many.return_value.inserted_ids = ["12345", "67890"]
        mock_mongo_client.return_value.__getitem__.return_value = mock_collection
        
        self.mongo_connection.insert_to_mongodb('test_collection', [{"key": "value1"}, {"key": "value2"}])
        mock_collection.insert_many.assert_called_once()

    @patch('mongodb_connection.MongoClient')
    def test_insert_failure(self, mock_mongo_client):
        """Test failure on inserting data."""
        mock_collection = MagicMock()
        mock_collection.insert_one.side_effect = Exception("Insertion failed")
        mock_mongo_client.return_value.__getitem__.return_value = mock_collection
        
        with self.assertLogs('mongodb_connection', level='ERROR') as log:
            self.mongo_connection.insert_to_mongodb('test_collection', {"key": "value"})
            self.assertIn('ERROR:mongodb_connection:Error inserting data into MongoDB: Insertion failed', log.output)

    def tearDown(self):
        """Clean up after each test."""
        self.mongo_connection.close()


if __name__ == '__main__':
    unittest.main()
