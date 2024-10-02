# https://leetcode.com/problems/product-price-at-a-given-date
import pandas as pd

def price_at_given_date(products_df: pd.DataFrame) -> pd.DataFrame:
    # Filter products where change_date is less than or equal to '2019-08-16'
    filtered_df = products_df[products_df['change_date'] <= '2019-08-16']

    # Create the last_prices DataFrame using groupby and idxmax to get the last prices
    last_prices = (
        filtered_df.loc[filtered_df.groupby('product_id')['change_date'].idxmax()]
        .reset_index(drop=True)
        .loc[:, ['product_id', 'new_price']]
    )

    # Create the distinct product IDs DataFrame
    dist_products = products_df[['product_id']].drop_duplicates()

    # Merge dist_products with last_prices
    result_df = pd.merge(dist_products, last_prices, on='product_id', how='left')

    # Fill NaN values in new_price with 10
    result_df['price'] = result_df['new_price'].fillna(10)

    # Select the final columns
    result_df = result_df[['product_id', 'price']]

    return result_df
