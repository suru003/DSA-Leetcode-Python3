# https://leetcode.com/problems/triangle-judgement/
import pandas as pd


# Define a function to check triangle condition
def is_triangle(row):
    if (row['x'] + row['y'] > row['z']) and \
            (row['y'] + row['z'] > row['x']) and \
            (row['x'] + row['z'] > row['y']):
        return 'Yes'
    else:
        return 'No'


def triangle_judgement(triangle_df: pd.DataFrame) -> pd.DataFrame:
    # Apply the function and create a new column "triangle"
    triangle_df['triangle'] = triangle_df.apply(is_triangle, axis=1)
    return triangle_df
