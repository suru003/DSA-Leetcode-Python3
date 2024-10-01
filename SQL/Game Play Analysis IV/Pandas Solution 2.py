# https://leetcode.com/problems/game-play-analysis-iv
import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Get the minimum event date for each player
    df_min_date = activity.groupby('player_id', as_index=False)['event_date'].min()

    # Merge the min event date back to the original DataFrame
    df_merged = pd.merge(activity, df_min_date, on='player_id', suffixes=('', '_min'))

    # Check if the event exists on the day after the minimum event date
    df_merged['score'] = df_merged.apply(lambda row: 1 if (row['event_date'] == row['event_date_min'] + pd.Timedelta(days=1)) else 0, axis=1)

    # Aggregate scores by player and compute the final average
    df_scores = df_merged.groupby('player_id')['score'].max().reset_index()

    # Compute the fraction and return as a DataFrame
    fraction = df_scores['score'].mean().round(2)
    result_df = pd.DataFrame({'fraction': [fraction]})
    return result_df
