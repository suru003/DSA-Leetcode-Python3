# https://leetcode.com/problems/fix-names-in-a-table/
import pandas as pd


def fix_names(users_df: pd.DataFrame) -> pd.DataFrame:
    users_df['name'] = users_df['name'].str[0].str.upper() + users_df['name'].str[1:].str.lower()

    """ Solution 2
    # Function to capitalize the first letter and lowercase the rest
    users_df['name'] = users_df['name'].apply(lambda x: x[0].upper() + x[1:].lower())
    """

    # Sorting by user_id
    users_df.sort_values(by='user_id', inplace=True)

    return users_df
