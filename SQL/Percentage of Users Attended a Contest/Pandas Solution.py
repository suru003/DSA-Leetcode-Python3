# https://leetcode.com/problems/percentage-of-users-attended-a-contest/
import pandas as pd


def users_percentage(users_df: pd.DataFrame, register_df: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Calculate the total number of users
    total_users = users_df['user_id'].count()

    # Step 2: Calculate percentage for each contest_id
    agg_df = register_df.groupby('contest_id').size().reset_index(name='count')
    agg_df['percentage'] = round((agg_df['count'] / total_users) * 100, 2)

    # Step 3: Sort the result
    agg_df = agg_df.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])

    agg_df.drop(columns=['count'], inplace=True)
    return agg_df
