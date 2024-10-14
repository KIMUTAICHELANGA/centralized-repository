import unittest
from unittest.mock import patch, MagicMock
from openalex_etl import OpenAlexETL

class TestOpenAlexETL(unittest.TestCase):

    @patch('openalex_etl.requests.get')
    def test_extract_data_success(self, mock_get):
        """Test successful data extraction from OpenAlex API."""
        mock_get.return_value.json.return_value = {'data': [{'id': '1', 'title': 'Test Title'}]}
        etl = OpenAlexETL()
        data = etl.extract_data()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    @patch('openalex_etl.requests.get')
    def test_extract_data_failure(self, mock_get):
        """Test failure on data extraction."""
        mock_get.return_value.raise_for_status.side_effect = Exception("API Error")
        etl = OpenAlexETL()
        with self.assertLogs('openalex_etl', level='ERROR') as log:
            etl.extract_data()
            self.assertIn('ERROR:openalex_etl:Failed to extract data from OpenAlex API: API Error', log.output)

    @patch('openalex_etl.MongoDBConnection.insert_to_mongodb')
    def test_transform_and_load(self, mock_insert):
        """Test transform and load functionality."""
        etl = OpenAlexETL()
        mock_insert.return_value = True  # Simulate successful insert
        sample_data = [{'id': '1', 'title': 'Test Title'}]
        
        etl.transform_and_load(sample_data)
        mock_insert.assert_called_once_with('openalex_collection', {'id': '1', 'title': 'Test Title'})

if __name__ == '__main__':
    unittest.main()
