import unittest
from unittest.mock import patch, MagicMock
from africannexus_etl import AfricanNexusETL

class TestAfricanNexusETL(unittest.TestCase):

    @patch('africannexus_etl.requests.get')
    def test_extract_data_success(self, mock_get):
        """Test successful data extraction from African Nexus API."""
        mock_get.return_value.json.return_value = {'data': [{'id': '1', 'name': 'Research Paper'}]}
        etl = AfricanNexusETL()
        data = etl.extract_data()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    @patch('africannexus_etl.requests.get')
    def test_extract_data_failure(self, mock_get):
        """Test failure on data extraction."""
        mock_get.return_value.raise_for_status.side_effect = Exception("API Error")
        etl = AfricanNexusETL()
        with self.assertLogs('africannexus_etl', level='ERROR') as log:
            etl.extract_data()
            self.assertIn('ERROR:africannexus_etl:Failed to extract data from African Nexus API: API Error', log.output)

    @patch('africannexus_etl.MongoDBConnection.insert_to_mongodb')
    def test_transform_and_load(self, mock_insert):
        """Test transform and load functionality."""
        etl = AfricanNexusETL()
        mock_insert.return_value = True  # Simulate successful insert
        sample_data = [{'id': '1', 'name': 'Research Paper'}]
        
        etl.transform_and_load(sample_data)
        mock_insert.assert_called_once_with('africannexus_collection', {'id': '1', 'name': 'Research Paper'})

if __name__ == '__main__':
    unittest.main()
