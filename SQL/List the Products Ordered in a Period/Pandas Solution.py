# https://leetcode.com/problems/list-the-products-ordered-in-a-period/
import pandas as pd


def list_products(products_df: pd.DataFrame, orders_df: pd.DataFrame) -> pd.DataFrame:
    # Filtering and joining
    result_df = orders_df[orders_df['order_date'].dt.month == 2]  # Filter for February
    result_df = result_df[result_df['order_date'].dt.year == 2020]  # Filter for year 2020

    # Join the two dataframes
    merged_df = pd.merge(result_df, products_df, on='product_id')

    # Group by product name and aggregate units
    grouped_df = merged_df.groupby('product_name').agg({'unit': 'sum'}).reset_index()

    # Filter based on unit having more than 99
    filtered_df = grouped_df[grouped_df['unit'] > 99]

    return filtered_df
