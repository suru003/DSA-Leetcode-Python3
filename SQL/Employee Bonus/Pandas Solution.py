# https://leetcode.com/problems/employee-bonus/
import pandas as pd


def employee_bonus(employee_df: pd.DataFrame, bonus_df: pd.DataFrame) -> pd.DataFrame:
    # Performing the LEFT JOIN
    result = employee_df.merge(bonus_df, on='empId', how='left')

    # Filtering the result
    filtered_result = result[(result['bonus'].isnull()) | (result['bonus'] < 1000)]

    # Selecting the desired columns
    final_result = filtered_result[['name', 'bonus']]

    return final_result
