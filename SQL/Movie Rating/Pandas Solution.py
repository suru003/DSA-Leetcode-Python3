# https://leetcode.com/problems/movie-rating/
import pandas as pd


def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Calculate the top user by the number of movie ratings
    top_user = movie_rating.merge(users, on='user_id', how='inner') \
        .groupby('name') \
        .size() \
        .reset_index(name='count') \
        .sort_values(by=['count', 'name'], ascending=[False, True]) \
        .head(1) \
        [['name']] \
        .rename(columns={'name': 'results'})

    # Step 2: Calculate the top movie rated in February 2020 by average rating
    movie_rating['created_at'] = pd.to_datetime(movie_rating['created_at'])
    top_movie = movie_rating[(movie_rating['created_at'].dt.month == 2) & (movie_rating['created_at'].dt.year == 2020)] \
        .merge(movies, on='movie_id', how='inner') \
        .groupby('title') \
        .agg(avg_rating=('rating', 'mean')) \
        .reset_index() \
        .sort_values(by=['avg_rating', 'title'], ascending=[False, True]) \
        .head(1) \
        [['title']] \
        .rename(columns={'title': 'results'})

    # Step 3: Union the top user and top movie results
    result = pd.concat([top_user, top_movie], ignore_index=True)

    return result
