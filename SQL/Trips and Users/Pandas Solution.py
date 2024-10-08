# https://leetcode.com/problems/trips-and-users/
import pandas as pd


def trips_and_users(trips_df: pd.DataFrame, users_df: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Filter valid users who are not banned
    valid_users = users_df[users_df['banned'].str.lower() == 'no']['users_id']

    # Step 2: Filter trips within date range and where both client and driver are valid
    filtered_trips = trips_df[
        (trips_df['request_at'] >= '2013-10-01') &
        (trips_df['request_at'] <= '2013-10-03') &
        (trips_df['client_id'].isin(valid_users)) &
        (trips_df['driver_id'].isin(valid_users))
        ]

    # Step 3: Calculate the Cancellation Rate
    filtered_trips['cancellation'] = filtered_trips['status'].str.lower().apply(lambda x: 1 if 'cancelled' in x else 0)

    # Step 4: Group by 'request_at' (Day) and calculate average cancellation rate
    cancellation_rate_df = filtered_trips.groupby('request_at').agg(
        cancellation_rate=('cancellation', 'mean')).reset_index()

    # Step 5: Round the cancellation rate
    cancellation_rate_df['cancellation_rate'] = cancellation_rate_df['cancellation_rate'].round(2)

    cancellation_rate_df.rename(
        columns={'request_at': 'day', 'cancellation_rate': 'cancellation rate'},
        inplace=True
    )

    return cancellation_rate_df
