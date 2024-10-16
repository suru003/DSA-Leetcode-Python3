from pyspark.sql import SparkSession
from pyspark.sql.functions import col, countDistinct, to_date, datediff, lit

# Initialize Spark session
spark = SparkSession.builder.appName("ActivityAnalysis").getOrCreate()

# Sample DataFrame (replace with actual Spark DataFrame)
data = [
    ("2019-07-01", 1),
    ("2019-07-02", 2),
    ("2019-07-27", 1),
    # Add actual data here...
]
columns = ["activity_date", "user_id"]
df = spark.createDataFrame(data, columns)

# Convert activity_date to date type
df = df.withColumn("activity_date", to_date(col("activity_date"), "yyyy-MM-dd"))

# Define reference date
reference_date = lit('2019-07-27')

# Apply the date filtering condition
filtered_df = df.filter(
    (datediff(reference_date, col("activity_date")) > -1) &
    (datediff(reference_date, col("activity_date")) < 30)
)

# Group by activity_date and count distinct user_id
result = filtered_df.groupBy("activity_date").agg(countDistinct("user_id").alias("active_users"))

# Rename the activity_date to day (optional in PySpark, but it can help match SQL naming)
result = result.withColumnRenamed("activity_date", "day")

# Show the result
result.show()
