from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Initialize SparkSession
spark = SparkSession.builder.appName("PySpark Example").getOrCreate()

# Sample DataFrame
data = [(1, 'a@example.com'),
        (2, 'b@example.com'),
        (3, 'a@example.com'),
        (4, 'b@example.com'),
        (5, 'c@example.com')]

columns = ['id', 'email']
df = spark.createDataFrame(data, columns)

# Define window spec
window_spec = Window.partitionBy("email").orderBy("id")

# Add a new column with the minimum id per email
df_min = df.withColumn("min_id", F.min("id").over(window_spec))

# Filter out the rows that do not have the minimum id
df_filtered = df_min.filter(F.col("id") == F.col("min_id")).drop("min_id")

# Show result
df_filtered.show()
