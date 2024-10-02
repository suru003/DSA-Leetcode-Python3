# https://leetcode.com/problems/average-selling-price/
import pandas as pd


def average_selling_price(prices_df: pd.DataFrame, units_sold_df: pd.DataFrame) -> pd.DataFrame:
    # Perform a left join
    merged_df = pd.merge(prices_df, units_sold_df, how='left', on='product_id')

    # Filter by date range
    filtered_df = merged_df[(merged_df['purchase_date'] >= merged_df['start_date']) &
                            (merged_df['purchase_date'] <= merged_df['end_date']) |
                            merged_df['purchase_date'].isna()]

    # Calculate weighted average price per product
    grouped_df = filtered_df.groupby('product_id').apply(lambda x:
                                                         pd.Series({'average_price': round(
                                                             (x['price'] * x['units']).sum() / x['units'].sum(), 2)}))

    # Replace NaN with 0 for products without sales
    grouped_df['average_price'] = grouped_df['average_price'].fillna(0)

    # Reset index to make 'product_id' a column again
    grouped_df = grouped_df.reset_index()

    return grouped_df
