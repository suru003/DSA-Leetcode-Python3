import pandas as pd
import numpy as np

# Custom rounding function that rounds 0.5 away from zero
def round_half_up(n):
    return np.floor(n + 0.5) if n > 0 else np.ceil(n - 0.5)

def count_employees(employees_df: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Create the aggregation (cte_agg equivalent)
    cte_agg = employees_df.groupby('reports_to').agg(
        reports_count=('employee_id', 'size'),
        average_age=('age', lambda x: round_half_up(x.mean()))  # Apply custom rounding here
    ).reset_index()

    # Step 2: Perform the join with the original dataframe
    result = employees_df.merge(cte_agg, how='inner', left_on='employee_id', right_on='reports_to')

    # Step 3: Select required columns and sort
    result = result[['employee_id', 'name', 'reports_count', 'average_age']].sort_values(by='employee_id')

    return result
