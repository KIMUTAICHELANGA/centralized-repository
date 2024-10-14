# africannexus_etl.py
import json
from api.africannexus_api import fetch_africannexus_data
from storage.mongodb.mongodb_connection import insert_to_mongodb
from utils.data_cleaning import clean_africannexus_data

def etl_africannexus():
    """
    ETL pipeline for ingesting data from African Nexus.
    """
    print("Extracting data from African Nexus...")
    data = fetch_africannexus_data('endpoint', {'params': 'value'})
    
    if data:
        print("Transforming data...")
        cleaned_data = clean_africannexus_data(data)
        
        print("Loading data into MongoDB...")
        for item in cleaned_data:
            insert_to_mongodb('africannexus_data', item)
    else:
        print("No data extracted from African Nexus.")

if __name__ == "__main__":
    etl_africannexus()
