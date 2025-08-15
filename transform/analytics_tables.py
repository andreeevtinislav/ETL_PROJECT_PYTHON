import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

def sales_by_region(df):
    try:
        data = df
        data['month'] = data['timestamp'].dt.strftime('%b')
        data = data.groupby(['region', 'month'])['total_sales'].sum().reset_index()
        data = data.rename(columns={'total_sales': 'total_sales_by_region'})
        logger.info("Sales by region data proccessed successfully.")
        return data
    except Exception as e:
        logger.error(f"Error creating sales by region data: {e}")
        raise

def sales_by_category_and_region(sales_df, product_df):
    try:
        merged_df = pd.merge(sales_df, product_df, on='product_id', how='left')
        merged_df = merged_df.groupby(['region', 'category'])['total_sales'].sum().reset_index()
        merged_df = merged_df[merged_df['total_sales'] > 1000]
        merged_df = merged_df.rename(columns={'total_sales': 'total_sales_by_category_and_region'})
        logger.info("Sales by category and region data processed successfully.")
        return merged_df
    except Exception as e:
        logger.error(f"Error creating sales by category and region data: {e}")
        raise
    


    