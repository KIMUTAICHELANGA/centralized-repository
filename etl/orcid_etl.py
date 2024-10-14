# orcid_etl.py
import json
from api.orcid_api import fetch_orcid_data
from storage.mongodb.mongodb_connection import insert_to_mongodb
from utils.data_cleaning import clean_orcid_data

def etl_orcid():
    """
    ETL pipeline for ingesting data from ORCID.
    """
    print("Extracting data from ORCID...")
    data = fetch_orcid_data('path/to/orcid/endpoint', {'params': 'value'})
    
    if data:
        print("Transforming data...")
        cleaned_data = clean_orcid_data(data)
        
        print("Loading data into MongoDB...")
        for item in cleaned_data:
            insert_to_mongodb('orcid_records', item)
    else:
        print("No data extracted from ORCID.")

if __name__ == "__main__":
    etl_orcid()
