import pandera.pandas as pa
from pandera.pandas import Column, DataFrameSchema, Check
import pandas as pd

sales_by_region_category_schema = DataFrameSchema({
    "region": Column(str, Check.isin(["North", "South", "East", "West", "Unknown"])),
    "total_sales_by_region": Column(float, Check.ge(0)),
    "month": Column(str, Check.str_length(3, 3))
})

sales_by_region_month_schema = DataFrameSchema({
    
    "region": Column(str, Check.isin(["North", "South", "East", "West", "Unknown"])),
    "total_sales_by_category_and_region": Column(float, Check.ge(0)),
    "category": Column(str, Check.str_length(1, 50))
})