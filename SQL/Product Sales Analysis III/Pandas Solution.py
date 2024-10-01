# https://leetcode.com/problems/product-sales-analysis-iii/
import pandas as pd

def sales_analysis(sales_df: pd.DataFrame, product_df: pd.DataFrame) -> pd.DataFrame:
    # Create the CTE equivalent
    cte_df = sales_df.groupby('product_id', as_index=False).agg(minyear=('year', 'min'))

    # Merge with the original Sales DataFrame
    result_df = pd.merge(sales_df, cte_df, left_on=['product_id', 'year'], right_on=['product_id', 'minyear'])

    # Select the relevant columns
    final_result_df = result_df[['product_id', 'year', 'quantity', 'price']]
    final_result_df.rename(columns = {'year': 'first_year'}, inplace = True)

    return final_result_df
