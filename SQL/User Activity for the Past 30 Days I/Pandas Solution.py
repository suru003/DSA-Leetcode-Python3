# https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
import pandas as pd

def user_activity(activity_df: pd.DataFrame) -> pd.DataFrame:
    # Define the reference date
    reference_date = pd.to_datetime('2019-07-27')

    # Filter the DataFrame based on the condition
    filtered_df = activity_df[((reference_date - activity_df['activity_date']).dt.days > -1) &
                              ((reference_date - activity_df['activity_date']).dt.days < 30)]

    # Group by 'activity_date' and count distinct 'user_id'
    result = filtered_df.groupby('activity_date')['user_id'].nunique().reset_index()

    # Rename columns for clarity
    result.columns = ['day', 'active_users']

    return result
