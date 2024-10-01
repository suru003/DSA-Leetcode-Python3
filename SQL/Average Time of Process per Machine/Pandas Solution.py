# https://leetcode.com/problems/average-time-of-process-per-machine/
import pandas as pd

def get_average_time(activity_df: pd.DataFrame) -> pd.DataFrame:
    # Create lagged column using groupby and shift
    activity_df['prev_timestamp'] = activity_df.sort_values('timestamp').groupby(['machine_id', 'process_id'])['timestamp'].shift(1)

    # Filter for 'end' activity_type and drop NaN values
    lagged_rows = activity_df[activity_df['activity_type'].str.lower() == 'end'].dropna()

    # Calculate processing time and group by machine_id
    result = lagged_rows.groupby('machine_id').agg(
        processing_time=('timestamp', lambda x: round((x - lagged_rows['prev_timestamp']).mean(), 3))
    ).reset_index()

    return result
