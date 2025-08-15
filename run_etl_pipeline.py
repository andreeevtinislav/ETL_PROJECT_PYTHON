import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from extract.extract_from_s3 import extract_sales_data, extract_product_metadata_json
from transform.cleaned_tables import cleaned_sales_data, cleaned_product_metadata
from transform.analytics_tables import sales_by_region, sales_by_category_and_region
from load.load_to_snowflake import load_cleaned_product_metadata_table, load_cleaned_sales_table, load_sales_by_region_table, load_sales_by_category_and_region_table
from validations.cleaned_table_validations import cleaned_sales_schema, cleaned_product_metadata_schema 
from validations.analytics_table_validations import sales_by_region_category_schema, sales_by_region_month_schema
import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        # raw data extraction
        raw_sales_df = extract_sales_data()
        raw_product_df = extract_product_metadata_json()
    except Exception as e:
        logger.error(f"Error during data extraction: {e}")
        raise
    try:
        # raw data loading
        load_cleaned_sales_table(raw_sales_df)
        load_cleaned_product_metadata_table(raw_product_df)
    except Exception as e:
        logger.error(f"Error during raw data loading: {e}")
        raise
    try:
        # data cleaning
        cleaned_sales_df = cleaned_sales_data(raw_sales_df)
        cleaned_product_df = cleaned_product_metadata(raw_product_df)
        cleaned_sales_schema.validate(cleaned_sales_df)
        cleaned_product_metadata_schema.validate(cleaned_product_df)
        logger.info("Cleaned data validation successful.")
        
    except Exception as e:
        logger.error(f"Error during data cleaning: {e}")
        raise
    try:
    # cleaned data loading
        load_cleaned_sales_table(cleaned_sales_df)
        load_cleaned_product_metadata_table(cleaned_product_df)
    except Exception as e:
        logger.error(f"Error during cleaned data loading: {e}")
    try:
    # analytics data creation
        sales_region_df = sales_by_region(cleaned_sales_df)
        sales_category_region_df = sales_by_category_and_region(cleaned_sales_df, cleaned_product_df)
        sales_by_region_category_schema.validate(sales_region_df)
        sales_by_region_month_schema.validate(sales_category_region_df)
        logger.info("Analytics data validation successful.")
    except Exception as e:
        logger.error(f"Error during analytics data creation: {e}")
    try:
    # analytics data loading
        load_sales_by_region_table(sales_region_df)
        load_sales_by_category_and_region_table(sales_category_region_df)
    except Exception as e:
        logger.error(f"Error during analytics data loading: {e}")
        raise


   
   
   
   
   

   
   
   
   
   