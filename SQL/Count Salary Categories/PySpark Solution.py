from pyspark.sql import SparkSession
from pyspark.sql.functions import when, sum as spark_sum

# Initialize Spark session
spark = SparkSession.builder.appName("SalaryCategories").getOrCreate()

# Sample data for the Accounts DataFrame
data = [
    (60000,), (45000,), (15000,), (32000,), (70000,), (25000,), (18000,), (51000,), (20000,), (50000,)
]
columns = ['income']

# Create Spark DataFrame
accounts_df = spark.createDataFrame(data, columns)

# High Salary
high_salary_count = accounts_df.select(spark_sum(when(accounts_df['income'] > 50000, 1).otherwise(0)).alias("accounts_count"))

# Low Salary
low_salary_count = accounts_df.select(spark_sum(when(accounts_df['income'] < 20000, 1).otherwise(0)).alias("accounts_count"))

# Average Salary
average_salary_count = accounts_df.select(spark_sum(when((accounts_df['income'] >= 20000) & (accounts_df['income'] <= 50000), 1).otherwise(0)).alias("accounts_count"))

# Combine results
categories = [("High Salary",), ("Low Salary",), ("Average Salary",)]
category_df = spark.createDataFrame(categories, ['category'])

counts_df = high_salary_count.union(low_salary_count).union(average_salary_count)

result_df = category_df.join(counts_df, category_df['category'] == counts_df['accounts_count'], "inner")
result_df.show()
