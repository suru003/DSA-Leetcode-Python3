from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Employee Filter") \
    .getOrCreate()

# Sample data creation for illustration
data = [(1, None, 25000), (2, 1, 28000), (3, 1, 32000), (4, None, 29000), (5, 6, 27000)]
columns = ['employee_id', 'manager_id', 'salary']
df_employees = spark.createDataFrame(data, columns)


def find_employees(spark_df):
    # Step 1: Filter employees with manager_id not null and salary < 30000
    filtered_employees = spark_df.filter(
        (F.col('manager_id').isNotNull()) &
        (F.col('salary') < 30000)
    )

    # Step 2: Get unique employee IDs
    unique_ids = spark_df.select('employee_id').distinct()

    # Step 3: Exclude employees who are managers from the filtered results
    final_result = filtered_employees.join(
        unique_ids,
        filtered_employees['manager_id'] == unique_ids['employee_id'],
        'left_anti'
    )

    # Step 4: Select only employee_id and sort the result
    final_result_sorted = final_result.select('employee_id').orderBy('employee_id')

    return final_result_sorted


# Call the function
result = find_employees(df_employees)
result.show()
