import pandas as pd


def find_employees(df_employees: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Filter employees with manager_id not null and salary < 30000
    filtered_employees = df_employees[
        (df_employees['manager_id'].notnull()) &
        (df_employees['salary'] < 30000)
        ]

    # Step 2: Find employee IDs
    uniques_ids = df_employees['employee_id'].unique()

    # Step 3: Exclude employees who are managers from the filtered results
    final_result = filtered_employees[~filtered_employees['manager_id'].isin(uniques_ids)]

    # Step 4: Select only employee_id and sort the result
    final_result_sorted = final_result[['employee_id']].sort_values(by='employee_id')
    return final_result_sorted