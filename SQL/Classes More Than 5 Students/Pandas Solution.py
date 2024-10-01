# https://leetcode.com/problems/classes-more-than-5-students/
import pandas as pd

def find_classes(df_courses: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'class': df_courses.groupby('class').filter(lambda x: len(x) > 4)['class'].unique()})
