# https://leetcode.com/problems/market-analysis-i/
import pandas as pd


def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    # Filter orders by year 2019 and group by buyer_id
    orders_2019 = orders[orders['order_date'].dt.year == 2019]
    cte_counts = orders_2019.groupby('buyer_id').agg(orders_in_2019=('item_id', 'count')).reset_index()

    # Merge with users (LEFT JOIN)
    result = pd.merge(users, cte_counts, left_on='user_id', right_on='buyer_id', how='left')

    # Fill missing orders_in_2019 with 0
    result['orders_in_2019'] = result['orders_in_2019'].fillna(0)

    # Final result
    result = result[['user_id', 'join_date', 'orders_in_2019']]
    result.rename(columns={'user_id': 'buyer_id'}, inplace=True)

    return result
