import unittest
from unittest.mock import patch, MagicMock
from orcid_etl import OrcidETL

class TestOrcidETL(unittest.TestCase):

    @patch('orcid_etl.requests.get')
    def test_extract_data_success(self, mock_get):
        """Test successful data extraction from ORCID API."""
        mock_get.return_value.json.return_value = {'data': [{'orcid': '0000-0001-2345-6789', 'name': 'John Doe'}]}
        etl = OrcidETL()
        data = etl.extract_data()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    @patch('orcid_etl.requests.get')
    def test_extract_data_failure(self, mock_get):
        """Test failure on data extraction."""
        mock_get.return_value.raise_for_status.side_effect = Exception("API Error")
        etl = OrcidETL()
        with self.assertLogs('orcid_etl', level='ERROR') as log:
            etl.extract_data()
            self.assertIn('ERROR:orcid_etl:Failed to extract data from ORCID API: API Error', log.output)

    @patch('orcid_etl.MongoDBConnection.insert_to_mongodb')
    def test_transform_and_load(self, mock_insert):
        """Test transform and load functionality."""
        etl = OrcidETL()
        mock_insert.return_value = True  # Simulate successful insert
        sample_data = [{'orcid': '0000-0001-2345-6789', 'name': 'John Doe'}]
        
        etl.transform_and_load(sample_data)
        mock_insert.assert_called_once_with('orcid_collection', {'orcid': '0000-0001-2345-6789', 'name': 'John Doe'})

if __name__ == '__main__':
    unittest.main()
