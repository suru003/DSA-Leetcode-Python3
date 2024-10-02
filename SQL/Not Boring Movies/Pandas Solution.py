# https://leetcode.com/problems/not-boring-movies/
import pandas as pd


def not_boring_movies(cinema_df: pd.DataFrame) -> pd.DataFrame:
    df_filtered = cinema_df[(cinema_df['id'] % 2 == 1) & (~cinema_df['description'].str.contains('boring'))]
    df_sorted = df_filtered.sort_values(by='rating', ascending=False)

    # Display the resulting DataFrame
    result = df_sorted[['id', 'movie', 'description', 'rating']]
    return result
