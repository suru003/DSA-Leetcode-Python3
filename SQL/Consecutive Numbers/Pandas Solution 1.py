# https://leetcode.com/problems/consecutive-numbers
import pandas as pd

def consecutive_numbers(df_logs: pd.DataFrame) -> pd.DataFrame:
    # Create plus_1 and plus_2 dataframes
    plus_1 = df_logs.copy()
    plus_1['id'] = plus_1['id'] + 1

    plus_2 = df_logs.copy()
    plus_2['id'] = plus_2['id'] + 2

    # Perform the join with the original dataframe
    result = df_logs.merge(plus_1, on=['id', 'num'], how='inner') \
                    .merge(plus_2, on=['id', 'num'], how='inner')

    # Select distinct 'num' values
    distinct_nums = result['num'].drop_duplicates()

    return pd.DataFrame({'ConsecutiveNums': distinct_nums})
