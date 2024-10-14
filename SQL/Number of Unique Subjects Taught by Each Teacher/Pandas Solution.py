# https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/
import pandas as pd


def count_unique_subjects(teacher_df: pd.DataFrame) -> pd.DataFrame:
    # Group by teacher_id and count distinct subject_id
    result = teacher_df.groupby('teacher_id')['subject_id'].nunique().reset_index(name='cnt')

    return result
