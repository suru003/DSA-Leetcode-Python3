# https://leetcode.com/problems/game-play-analysis-i/
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Group by player_id and get the first login (min event_date)
    result = activity.groupby('player_id').agg(first_login=('event_date', 'min')).reset_index()

    return result