from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, lower, substring, length, concat

# Create Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Sample data
data = [(1, 'john'), (2, 'susan'), (3, 'michael')]
columns = ['user_id', 'name']
df = spark.createDataFrame(data, columns)

df = df.select(
    col('user_id'),
    concat(
        upper(substring(col('name'), 1, 1)),  # Capitalize the first letter
        lower(substring(col('name'), 2, length(col('name'))))  # Lowercase the rest of the name
    ).alias('name')  # Alias the resulting column as 'name'
).orderBy('user_id')  # Order by user_id

# Sort by user_id
df = df.orderBy('user_id')

# Show result
df.show()
