import pandas as pd
import math

# Sample data
data = {
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['John', 'Jane', 'Mike', 'Alice', 'Bob'],
    'reports_to': [None, 1, 1, 2, 3],
    'age': [45, 30, 40, 25, 35]
}

df = pd.DataFrame(data)

# Custom rounding function
def custom_round(x):
    return math.floor(x) if x - math.floor(x) < 0.5 else math.ceil(x)

# Step 1: Create the aggregation (cte_agg equivalent)
cte_agg = df.groupby('reports_to').agg(
    reports_count=('employee_id', 'size'),
    average_age=('age', lambda x: custom_round(x.mean()))
).reset_index()

# Step 2: Perform the join with the original dataframe
result = df.merge(cte_agg, how='left', left_on='employee_id', right_on='reports_to')

# Step 3: Select required columns and sort
result = result[['employee_id', 'name', 'reports_count', 'average_age']].sort_values(by='employee_id')

# Display the result
print(result)
