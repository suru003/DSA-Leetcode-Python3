from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, lower, substring

# Create Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Sample data
data = [(1, 'john'), (2, 'susan'), (3, 'michael')]
columns = ['user_id', 'name']
df = spark.createDataFrame(data, columns)

# Apply transformations
df = df.withColumn('name', upper(substring(col('name'), 1, 1)) + lower(substring(col('name'), 2, len(col('name')))))

# Sort by user_id
df = df.orderBy('user_id')

# Show result
df.show()
