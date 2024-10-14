# dspace_etl.py
import json
from api.dspace_api import fetch_dspace_data
from storage.mongodb.mongodb_connection import insert_to_mongodb
from utils.data_cleaning import clean_dspace_data

def etl_dspace():
    """
    ETL pipeline for ingesting data from DSpace.
    """
    print("Extracting data from DSpace...")
    data = fetch_dspace_data('endpoint', {'params': 'value'})
    
    if data:
        print("Transforming data...")
        cleaned_data = clean_dspace_data(data)
        
        print("Loading data into MongoDB...")
        for item in cleaned_data:
            insert_to_mongodb('dspace_records', item)
    else:
        print("No data extracted from DSpace.")

if __name__ == "__main__":
    etl_dspace()
