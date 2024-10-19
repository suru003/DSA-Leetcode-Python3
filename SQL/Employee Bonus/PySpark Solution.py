# https://leetcode.com/problems/employee-bonus/
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("Employee Bonus Analysis").getOrCreate()

# Sample DataFrames for Employee and Bonus
data_employee = [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie'), (4, 'David')]
data_bonus = [(1, 1500), (2, 800), (3, 1200)]

# Creating DataFrames
df_employee = spark.createDataFrame(data_employee, ['empId', 'name'])
df_bonus = spark.createDataFrame(data_bonus, ['empId', 'bonus'])

# Performing the LEFT JOIN
result = df_employee.alias('df1').join(df_bonus.alias('df2'), on='empId', how='left')\
        .select(col('df1.empId').alias('empId')
            , col('df2.bonus').alias('bonus')
            , col('df2.empId').alias('bonusId'))

# Filtering the result
filtered_result = result.filter(col('bonusId').isNull() | (col('bonus') < 1000))

# Selecting the desired columns
final_result = filtered_result.select(col('empId').alias('name'), 'bonus')
final_result.show()
