from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col, sum as spark_sum

# Initialize Spark session
spark = SparkSession.builder.appName("SalaryCategories").getOrCreate()

# Sample data for the Accounts DataFrame
data = [
    (60000,), (45000,), (15000,), (32000,), (70000,), (25000,), (18000,), (51000,), (20000,), (50000,), (50000,), (20000,)
]
columns = ['income']

# Create Spark DataFrame
accounts_df = spark.createDataFrame(data, columns)

# High Salary
high_salary_count = accounts_df.filter(col('income') > 50000).count()

# Low Salary
low_salary_count = accounts_df.filter(col('income') < 20000).count()

# Average Salary
average_salary_count = accounts_df.filter(col('income').between(20000, 50000)).count()

# Combine results
result_df = spark.createDataFrame([
    ('High Salary', high_salary_count),
    ('Low Salary', low_salary_count),
    ('Average Salary', average_salary_count)
], ['category', 'accounts_count'])

result_df.show()
