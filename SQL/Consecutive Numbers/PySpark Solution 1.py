from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("PySpark SQL Example").getOrCreate()

# Sample Data
data = [(1, 1), (2, 2), (3, 3), (4, 3), (5, 4)]
df_logs = spark.createDataFrame(data, ["id", "num"])

# Create plus_1 and plus_2 DataFrames
df_plus_1 = df_logs.withColumn("id", col("id") + 1)
df_plus_2 = df_logs.withColumn("id", col("id") + 2)

# Perform the join with the original dataframe
df_result = df_logs.alias("l") \
    .join(df_plus_1.alias("p1"), (col("l.id") == col("p1.id")) & (col("l.num") == col("p1.num")), "inner") \
    .join(df_plus_2.alias("p2"), (col("l.id") == col("p2.id")) & (col("l.num") == col("p2.num")), "inner")

# Select distinct 'num' values
df_distinct_nums = df_result.select(col("l.num").alias("ConsecutiveNums")).distinct()

# Show the result
df_distinct_nums.show()
