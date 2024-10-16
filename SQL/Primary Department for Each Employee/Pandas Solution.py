# https://leetcode.com/problems/primary-department-for-each-employee/
import pandas as pd

def find_primary_department(employee_df: pd.DataFrame) -> pd.DataFrame:
    # Create row number using groupby and rank based on the 'primary_flag' column
    employee_df['row_num'] = employee_df.groupby('employee_id')['primary_flag'].rank(method='first', ascending=False)

    # Filter rows where row_num is 1
    result_df = employee_df[employee_df['row_num'] == 1][['employee_id', 'department_id']]

    return result_df
