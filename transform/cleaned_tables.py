import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import logging

logger = logging.getLogger(__name__)

def cleaned_sales_data(df):
    try:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['region'] = df['region'].str.capitalize()
        df = df[df['price'] >= 0]
        df = df[df['total_sales'] >= 0]
        df['region'] = df['region'].fillna('Unknown')
        df['total_sales'] = df['total_sales'].round(2)
        df = df.drop_duplicates(subset=['product_id'], keep='first')
        logger.info("Cleaned sales data processed successfully.")
        return df
    except Exception as e:
        logger.error(f"Error transforming sales data: {e}")
        raise

def cleaned_product_metadata(df):
    try:
        df['rating'] = df['rating'].apply(np.ceil)
        df['brand'] = df['brand'].str.replace('Brand','', regex=True)
        df['category'] = df['category'].str.capitalize()
        df = df.sort_values(by='product_id')
        logger.info("Cleaned product metadata processed successfully.")
        return df
    except Exception as e:
        logger.error(f"Error transforming product metadata: {e}")
        raise