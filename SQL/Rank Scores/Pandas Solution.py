# https://leetcode.com/problems/rank-scores/
import pandas as pd

def order_scores(scores_df: pd.DataFrame) -> pd.DataFrame:
    # Apply dense rank
    scores_df['rank'] = scores_df['score'].rank(method='dense', ascending=False).astype(int)

    # Sort by score in descending order
    scores_df = scores_df.sort_values('score', ascending=False).reset_index(drop=True)

    scores_df.drop(columns = ['id'], inplace = True)
    return scores_df
