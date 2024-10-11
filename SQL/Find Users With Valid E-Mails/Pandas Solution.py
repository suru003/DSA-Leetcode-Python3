# https://leetcode.com/problems/find-users-with-valid-e-mails
import pandas as pd


def valid_emails(users_df: pd.DataFrame) -> pd.DataFrame:
    # Applying the filter
    filtered_df = users_df[users_df['mail'].str.contains(r'^[a-zA-Z]+[a-zA-Z0-9_.-]*@leetcode\.com$', regex=True)]

    return filtered_df
