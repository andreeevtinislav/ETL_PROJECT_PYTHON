import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.setting import S3_BUCKET, FILE_PATH_CSV, s3_client
from io import StringIO
import logging

logger = logging.getLogger(__name__)


def extract_sales_data():
    try:
        response = s3_client.get_object(Bucket=S3_BUCKET, Key=FILE_PATH_CSV)
        df = pd.read_csv(response["Body"])
        logger.info("Sales data extracted from S3 successfully.")
        return df
    except Exception as e:
        logger.error(f"Error extracting sales data: {e}")
        raise
        

def extract_product_metadata_json():
    try:
        response = s3_client.get_object(Bucket=S3_BUCKET, Key='product_metadata.json')
        json_data = response["Body"].read().decode('utf-8')
        df = pd.read_json(StringIO(json_data))
        logger.info("Product metadata extracted from S3 successfully.")
        return df
    except Exception as e:
        logger.error(f"Error extracting product metadata: {e}")
        raise
