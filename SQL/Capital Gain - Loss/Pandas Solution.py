# https://leetcode.com/problems/capital-gainloss/description/
import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    # Perform the transformation
    stocks['capital_gain_loss'] = stocks.apply(lambda x: -x['price'] if x['operation'] == 'Buy' else x['price'], axis=1)

    # Group by 'stock_name' and sum 'capital_gain_loss'
    result = stocks.groupby('stock_name')['capital_gain_loss'].sum().reset_index()

    return result
