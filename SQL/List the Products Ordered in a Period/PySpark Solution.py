from pyspark.sql import SparkSession
from pyspark.sql.functions import col, month, year, sum

# Initialize Spark session
spark = SparkSession.builder.appName("Query Example").getOrCreate()

# Sample DataFrames (assuming orders_df and products_df are Spark DataFrames)
orders_data = [
    (1, 50, '2020-02-01'),
    (2, 100, '2020-02-15'),
    (1, 150, '2020-02-20'),
    (3, 80, '2020-03-01')
]
products_data = [
    (1, 'Product A'),
    (2, 'Product B'),
    (3, 'Product C')
]

orders_df = spark.createDataFrame(orders_data, ['product_id', 'unit', 'order_date'])
products_df = spark.createDataFrame(products_data, ['product_id', 'product_name'])

# Convert order_date to date format
orders_df = orders_df.withColumn('order_date', col('order_date').cast('date'))

# Filter for February 2020
filtered_orders_df = orders_df.filter((month('order_date') == 2) & (year('order_date') == 2020))

# Join the two DataFrames on product_id
joined_df = filtered_orders_df.join(products_df, on='product_id', how='inner')

# Group by product name and aggregate the unit values
grouped_df = joined_df.groupBy('product_name').agg(sum('unit').alias('unit_sum'))

# Filter where sum of units is greater than 99
result_df = grouped_df.filter(col('unit_sum') > 99)

# Show the result
result_df.show()
