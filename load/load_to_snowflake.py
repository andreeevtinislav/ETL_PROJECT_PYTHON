import pandas as pd
import logging
from config.setting import engine


def load_raw_sales_table(df):
    try:
        df.to_sql('sales_north_raw', con=engine, if_exists='replace', index=False, schema='RAW')
        logging.info("Raw sales data loaded into Snowflake successfully.")
    except Exception as e:
        logging.error(f"Error loading raw sales data into Snowflake: {e}")
        raise
def load_raw_product_metadata_table(df):
    try:
        df.to_sql('product_metadata_raw', con=engine, if_exists='replace', index=False, schema='RAW')
        logging.info("Raw product metadata loaded into Snowflake successfully.")
    except Exception as e:
        logging.error(f"Error loading raw product metadata into Snowflake: {e}")
        raise
def load_cleaned_sales_table(df):
    try:
        df.to_sql('sales_north_transformed', con=engine, if_exists='replace', index=False, schema='CLEANSED')
        logging.info("Transformed sales data loaded into Snowflake successfully.")
    except Exception as e:
        logging.error(f"Error loading transformed sales data into Snowflake: {e}")
        raise
def load_cleaned_product_metadata_table(df):
    try:
        df.to_sql('product_metadata_transformed', con=engine, if_exists='replace', index=False, schema='CLEANSED')
        logging.info("Transformed product metadata loaded into Snowflake successfully.")
    except Exception as e:
        logging.error(f"Error loading transformed product metadata into Snowflake: {e}")
        raise
def load_sales_by_region_table(df):
    try:
        df.to_sql('sales_by_region', con=engine, if_exists='replace', index=False, schema='ANALYTICS')
        logging.info("Sales by region data loaded into Snowflake successfully.")
    except Exception as e:
        logging.error(f"Error loading sales by region data into Snowflake: {e}")
        raise
def load_sales_by_category_and_region_table(df):
    try:
        df.to_sql('sales_by_category_and_region', con=engine, if_exists='replace', index=False, schema='ANALYTICS')
        logging.info("Sales by category and region data loaded into Snowflake successfully.")
    except Exception as e:
        logging.error(f"Error loading sales by category and region data into Snowflake: {e}")
        raise
        
    
    