from pyspark.sql import SparkSession
from pyspark.sql.functions import min

# Initialize Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Sample data
data = [(1, '2024-09-01'), (2, '2024-09-02'), (1, '2024-09-03'),
        (3, '2024-09-04'), (2, '2024-09-05'), (1, '2024-09-06')]

# Create DataFrame
columns = ['player_id', 'event_date']
df = spark.createDataFrame(data, columns)

# Convert event_date to DateType if necessary
df = df.withColumn("event_date", df["event_date"].cast("date"))

# Group by player_id and get the first login (min event_date)
result = df.groupBy("player_id").agg(min("event_date").alias("first_login"))

# Show the result
result.show()
