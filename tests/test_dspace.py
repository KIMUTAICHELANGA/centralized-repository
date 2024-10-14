import unittest
from unittest.mock import patch, MagicMock
from dspace_etl import DSpaceETL

class TestDSpaceETL(unittest.TestCase):

    @patch('dspace_etl.requests.get')
    def test_extract_data_success(self, mock_get):
        """Test successful data extraction from DSpace API."""
        mock_get.return_value.json.return_value = {'data': [{'id': '1', 'title': 'DSpace Paper'}]}
        etl = DSpaceETL()
        data = etl.extract_data()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    @patch('dspace_etl.requests.get')
    def test_extract_data_failure(self, mock_get):
        """Test failure on data extraction."""
        mock_get.return_value.raise_for_status.side_effect = Exception("API Error")
        etl = DSpaceETL()
        with self.assertLogs('dspace_etl', level='ERROR') as log:
            etl.extract_data()
            self.assertIn('ERROR:dspace_etl:Failed to extract data from DSpace API: API Error', log.output)

    @patch('dspace_etl.MongoDBConnection.insert_to_mongodb')
    def test_transform_and_load(self, mock_insert):
        """Test transform and load functionality."""
        etl = DSpaceETL()
        mock_insert.return_value = True  # Simulate successful insert
        sample_data = [{'id': '1', 'title': 'DSpace Paper'}]
        
        etl.transform_and_load(sample_data)
        mock_insert.assert_called_once_with('dspace_collection', {'id': '1', 'title': 'DSpace Paper'})

if __name__ == '__main__':
    unittest.main()
