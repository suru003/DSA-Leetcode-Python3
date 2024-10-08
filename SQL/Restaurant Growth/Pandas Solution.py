# https://leetcode.com/problems/restaurant-growth/
import pandas as pd


def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    # Group by 'visited_on' and calculate sum (in case there are multiple entries for each date)
    df_grouped = customer.groupby('visited_on', as_index=False).sum()

    # Calculate the rolling sum and rolling average (7-day window, including current row)
    df_grouped['rolling_sum'] = df_grouped['amount'].rolling(window=7, min_periods=1).sum()
    df_grouped['rolling_avg'] = df_grouped['amount'].rolling(window=7, min_periods=1).mean().round(2)

    # Apply the OFFSET equivalent (skip first 6 rows)
    df_result = df_grouped.iloc[6:].reset_index(drop=True)

    df_result.drop(columns=["customer_id", "name", "amount"], inplace=True)
    df_result.rename(columns={"rolling_sum": "amount", "rolling_avg": "average_amount"}, inplace=True)
    return df_result