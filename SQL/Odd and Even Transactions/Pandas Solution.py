# https://leetcode.com/problems/odd-and-even-transactions/
import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    # Add odd_sum and even_sum columns
    transactions['odd_sum'] = transactions.apply(lambda x: x['amount'] if x['amount'] % 2 == 1 else 0, axis=1)
    transactions['even_sum'] = transactions.apply(lambda x: x['amount'] if x['amount'] % 2 == 0 else 0, axis=1)

    # Group by transaction_date and calculate sums
    result = transactions.groupby('transaction_date').agg({'odd_sum': 'sum', 'even_sum': 'sum'}).reset_index()

    # Sort by transaction_date
    result = result.sort_values(by='transaction_date')

    return result
