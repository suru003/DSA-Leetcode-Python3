from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Initialize Spark session
spark = SparkSession.builder.appName("ProcessingTime").getOrCreate()

# Sample data similar to the Activity table
data = [
    (1, 101, 'start', '2024-09-01 08:00:00'),
    (1, 101, 'end', '2024-09-01 08:10:00'),
    (1, 101, 'end', '2024-09-01 08:20:00'),
    (2, 202, 'start', '2024-09-01 09:00:00'),
    (2, 202, 'end', '2024-09-01 09:30:00'),
]

# Create DataFrame
columns = ['machine_id', 'process_id', 'activity_type', 'timestamp']
df = spark.createDataFrame(data, columns)

# Convert timestamp column to TimestampType
df = df.withColumn("timestamp", F.to_timestamp(df["timestamp"]))

# Create window specification
window_spec = Window.partitionBy("machine_id", "process_id").orderBy("timestamp")

# Create lagged column
lagged_rows = df.withColumn("prev_timestamp", F.lag("timestamp").over(window_spec))

# Filter for 'end' activity_type and drop nulls
lagged_rows = lagged_rows.filter(F.lower(df.activity_type) == 'end').dropna()

# Calculate processing time and group by machine_id
result = lagged_rows.groupBy("machine_id").agg(
    F.round(F.avg(F.col("timestamp").cast("long") - F.col("prev_timestamp").cast("long")), 3).alias("processing_time")
)

result.show()
