from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Initialize Spark Session
spark = SparkSession.builder.appName("SQL Conversion").getOrCreate()

# Sample DataFrame
data = [("2024-09-27", "A"),
        ("2024-09-27", "B"),
        ("2024-09-28", "A"),
        ("2024-09-28", "C"),
        ("2024-09-28", "D")]

columns = ["sell_date", "product"]

df = spark.createDataFrame(data, columns)

# Grouping by sell_date
result = df.groupBy("sell_date").agg(
    F.countDistinct("product").alias("num_sold"),  # Count distinct products
    F.collect_set("product").alias("products")     # Collect distinct products into a list
)

# Concatenate and sort products, then order by sell_date
result = result.withColumn(
    "products", F.expr("array_sort(products)")  # Sort the array of products
).withColumn(
    "products", F.expr("concat_ws(',', products)")  # Join array into a string separated by commas
).orderBy("sell_date")

result.show(truncate=False)
