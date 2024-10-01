# https://leetcode.com/problems/customers-who-bought-all-products/
import pandas as pd


def find_customers(df_customer: pd.DataFrame, df_product: pd.DataFrame) -> pd.DataFrame:
    # Total count of products
    target_count = df_product.shape[0]

    # Aggregate count of unique products per customer
    agg_count = df_customer.groupby(['customer_id', 'product_key']).size().reset_index(name='unique_count')

    # Final selection based on the HAVING condition
    result = agg_count.groupby('customer_id').filter(lambda x: x['unique_count'].count() == target_count)

    # Select only the customer_id
    final_result = result['customer_id'].unique()

    return pd.DataFrame({'customer_id': final_result})
