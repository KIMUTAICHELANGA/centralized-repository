import logging

def validate_data(data, schema):
    """Validates incoming data against a defined schema.
    
    Args:
        data (list): List of dictionaries representing raw data.
        schema (dict): Schema defining the expected structure of the data.

    Returns:
        bool: True if data is valid, False otherwise.
    """
    for record in data:
        for field, expected_type in schema.items():
            if field not in record:
                logging.warning(f'Missing field: {field} in record: {record}')
                return False
            if not isinstance(record[field], expected_type):
                logging.warning(f'Field {field} in record {record} is not of type {expected_type.__name__}')
                return False
    return True
