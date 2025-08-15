import pandas as pd
import boto3
from sqlalchemy import create_engine
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler('etl_pipeline.log'),logging.StreamHandler(sys.stdout)])

logger = logging.getLogger(__name__)

# s3 DETAILS
S3_BUCKET = 'engineering-class'
FILE_PATH_CSV = 'sales_north.csv'

# AWS S3 Client
try:
    s3_client = boto3.client(
        "s3",
        aws_access_key_id='ENTER_YOUR_AWS_ACCESS_KEY',
        aws_secret_access_key='ENTER_YOUR_AWS_SECRET_ACCESS_KEY'
        )
except Exception as e:
    logger.error(f"Error creating S3 client: {e}")
    raise
# SQLAlchemy SNOWFLAKE Engine
try:
    engine = create_engine(
        'ENTER_YOUR_SNOWFLAKE_CONNECTION_STRING',
    )
except Exception as e:
    logger.error(f"Error creating SQLAlchemy engine: {e}")
    raise