# https://leetcode.com/problems/classes-more-than-5-students/
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Create a Spark session
spark = SparkSession.builder.appName("PySpark Example").getOrCreate()

# Sample DataFrame
data = [("Math",), ("Science",), ("Math",), ("English",), ("Math",),
        ("Science",), ("History",), ("Math",), ("History",),
        ("Science",), ("Math",), ("History",), ("Math",)]
columns = ['class']
df_courses = spark.createDataFrame(data, columns)

# Group by 'class' and filter with count > 4
result = df_courses.groupBy('class').agg(F.count('*').alias('count')) \
                   .filter(F.col('count') > 4) \
                   .select('class')

# Show the result
result.show()
