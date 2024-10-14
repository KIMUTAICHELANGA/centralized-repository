# openalex_etl.py
import json
from api.openalex_api import fetch_openalex_data
from storage.mongodb.mongodb_connection import insert_to_mongodb
from utils.data_cleaning import clean_openalex_data

def etl_openalex():
    """
    ETL pipeline for ingesting data from OpenAlex.
    """
    print("Extracting data from OpenAlex...")
    data = fetch_openalex_data('works', {'filter': 'is_oa:true'})
    
    if data:
        print("Transforming data...")
        cleaned_data = clean_openalex_data(data)
        
        print("Loading data into MongoDB...")
        for item in cleaned_data:
            insert_to_mongodb('openalex_works', item)
    else:
        print("No data extracted from OpenAlex.")

if __name__ == "__main__":
    etl_openalex()
