# https://leetcode.com/problems/find-followers-count/
import pandas as pd


def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    # Group by user_id and count the number of followers
    followers_count_df = followers.groupby('user_id').size().reset_index(name='followers_count')

    # Sort by user_id
    followers_count_df = followers_count_df.sort_values(by='user_id')

    return followers_count_df
