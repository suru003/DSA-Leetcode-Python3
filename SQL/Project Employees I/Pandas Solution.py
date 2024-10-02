# https://leetcode.com/problems/project-employees-i
import pandas as pd

def project_employees_i(project_df: pd.DataFrame, employee_df: pd.DataFrame) -> pd.DataFrame:
    # Perform the join
    merged_df = pd.merge(project_df, employee_df, on='employee_id')

    # Group by 'project_id' and calculate the average experience
    result_df = merged_df.groupby('project_id').agg(average_years=('experience_years', lambda x: round(x.mean(), 2))).reset_index()

    return result_df
