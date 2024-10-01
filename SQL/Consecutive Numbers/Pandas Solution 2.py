# https://leetcode.com/problems/consecutive-numbers
import pandas as pd


def consecutive_numbers(df: pd.DataFrame) -> pd.DataFrame:
    # Use shift() to create columns similar to LAG and LEAD
    df['PrevNum'] = df['num'].shift(1)
    df['NextNum'] = df['num'].shift(-1)

    # Filter rows where the current number is the same as both the previous and next number
    consecutive_nums_df = df[(df['num'] == df['PrevNum']) & (df['num'] == df['NextNum'])]

    # Select distinct 'num' values and return the DataFrame
    distinct_consecutive_nums_df = consecutive_nums_df[['num']].drop_duplicates().reset_index(drop=True)
    distinct_consecutive_nums_df.rename(columns={'num': 'ConsecutiveNums'}, inplace=True)

    return distinct_consecutive_nums_df
