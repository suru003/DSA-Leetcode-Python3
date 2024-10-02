from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Initialize Spark session
spark = SparkSession.builder.appName("SQL_Equivalent").getOrCreate()

# Sample data for projects
projects = [(1, 101), (1, 102), (2, 103), (2, 104), (3, 105)]
projects_df = spark.createDataFrame(projects, ['project_id', 'employee_id'])

# Sample data for employees
employees = [(101, 5), (102, 10), (103, 7), (104, 3), (105, 6)]
employees_df = spark.createDataFrame(employees, ['employee_id', 'experience_years'])

# Perform the join
merged_df = projects_df.join(employees_df, on='employee_id')

# Group by 'project_id' and calculate the average experience, rounded to 2 decimal places
result_df = merged_df.groupBy('project_id').agg(F.round(F.avg('experience_years'), 2).alias('average_years'))

result_df.show()
