import os
import logging
from utils.logger import setup_logger
from storage.mongodb.mongodb_connection import connect_to_mongodb
from etl.openalex_etl import run_openalex_etl
from etl.orcid_etl import run_orcid_etl
from etl.africannexus_etl import run_africannexus_etl
from etl.dspace_etl import run_dspace_etl

def main():
    """Main function to trigger the ETL process."""
    # Setup logging
    setup_logger()
    logging.info("ETL process started.")

    # Connect to MongoDB
    mongo_client = connect_to_mongodb()
    
    if mongo_client is None:
        logging.error("Failed to connect to MongoDB. Exiting.")
        return

    # Run ETL for OpenAlex
    logging.info("Starting ETL for OpenAlex.")
    run_openalex_etl(mongo_client)
    
    # Run ETL for ORCID
    logging.info("Starting ETL for ORCID.")
    run_orcid_etl(mongo_client)

    # Run ETL for African Nexus
    logging.info("Starting ETL for African Nexus.")
    run_africannexus_etl(mongo_client)

    # Run ETL for DSpace
    logging.info("Starting ETL for DSpace.")
    run_dspace_etl(mongo_client)

    logging.info("ETL process completed successfully.")

if __name__ == "__main__":
    main()
