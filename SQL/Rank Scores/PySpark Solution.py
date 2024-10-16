from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import col, dense_rank

# Initialize Spark session
spark = SparkSession.builder.appName("DenseRankExample").getOrCreate()

# Sample data
data = [(100,), (90,), (90,), (80,), (70,)]
columns = ["score"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Define window specification
window_spec = Window.orderBy(col("score").desc())

# Apply dense rank
df = df.withColumn("rank", dense_rank().over(window_spec))

# Sort by score in descending order
df = df.orderBy(col("score").desc())

# Show result
df.show()
