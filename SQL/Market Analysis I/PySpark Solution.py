from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, count, coalesce, lit

# Initialize Spark session
spark = SparkSession.builder.appName("User Orders").getOrCreate()

# Sample data for Orders and Users
orders_data = [(1, 101, '2019-01-15'),
               (2, 102, '2019-06-01'),
               (1, 103, '2019-08-22'),
               (3, 104, '2020-02-15'),
               (2, 105, '2019-11-30')]

users_data = [(1, '2018-01-01'),
              (2, '2018-03-15'),
              (3, '2019-05-30'),
              (4, '2020-01-10')]

# Create DataFrames
orders_df = spark.createDataFrame(orders_data, ["buyer_id", "item_id", "order_date"])
users_df = spark.createDataFrame(users_data, ["user_id", "join_date"])

# Convert order_date to date type
orders_df = orders_df.withColumn("order_date", col("order_date").cast("date"))

# Filter for orders in 2019 and group by buyer_id
orders_2019 = orders_df.filter(year(col("order_date")) == 2019)
cte_counts = orders_2019.groupBy("buyer_id").agg(count("item_id").alias("orders_in_2019"))

# Perform a LEFT JOIN with Users DataFrame
result = users_df.join(cte_counts, users_df.user_id == cte_counts.buyer_id, "left")

# Replace null values with 0 in the orders_in_2019 column
result = result.withColumn("orders_in_2019", coalesce(col("orders_in_2019"), lit(0)))

# Select final columns and show the result
result.select("user_id", "join_date", "orders_in_2019").show()
