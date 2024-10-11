# https://leetcode.com/problems/group-sold-products-by-the-date/
import pandas as pd

def categorize_products(activities_df: pd.DataFrame) -> pd.DataFrame:
    # Grouping by sell_date and applying the logic
    result = activities_df.groupby('sell_date').agg(
        num_sold=('product', lambda x: x.nunique()),  # Count distinct products
        products=('product', lambda x: ','.join(sorted(x.unique())))  # String aggregation of distinct products
    ).reset_index()

    # Sorting by sell_date
    result = result.sort_values(by='sell_date')

    return result
