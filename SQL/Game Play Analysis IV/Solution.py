# https://leetcode.com/problems/game-play-analysis-iv
import pandas as pd


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Get the earliest event date for each player
    df_min_date = activity.groupby('player_id')['event_date'].min().reset_index()

    # Step 2: Define a function to check for the condition (next-day event)
    def check_next_day(player_id, min_date):
        # Check if the player's events contain the next day after min_date
        next_day = min_date + pd.Timedelta(days=1)
        exists_next_day = activity[(activity['player_id'] == player_id) \
                                   & (activity['event_date'] == next_day)].any()

        return 1 if exists_next_day.any() else 0

    # Step 3: Apply the function to get the 'score' for each player
    df_min_date['score'] = df_min_date.apply(lambda row: check_next_day(row['player_id'], row['event_date']), axis=1)

    # Step 4: Compute the average of the 'score'
    fraction = df_min_date['score'].mean().round(2)

    # Step 5: Return the result as a DataFrame
    result_df = pd.DataFrame({'fraction': [fraction]})
    return result_df
