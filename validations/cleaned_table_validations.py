import pandera as pa
from pandera.pandas import Column, DataFrameSchema, Check
import pandas as pd


cleaned_sales_schema = pa.DataFrameSchema({
      "sales_id": pa.Column(int, Check.ge(0), unique=True),
      "product_id": pa.Column(int, Check.ge(0), unique=True),
      "region": pa.Column(str, Check.isin(["North", "South", "East", "West", "Unknown"])),
      "quantity": pa.Column(int, Check.ge(0)),
      "price": pa.Column(float, Check.ge(0)),
      "timestamp": pa.Column(pd.Timestamp),
      "total_sales": pa.Column(float, Check.ge(0))
})

cleaned_product_metadata_schema = pa.DataFrameSchema({
      "product_id": pa.Column(int, Check.ge(0), unique=True),
      "category": pa.Column(str, Check.str_length(1, 50)),
      "brand": pa.Column(str, Check.str_length(1, 50)),
      "rating": pa.Column(float, Check.in_range(0,5))
})