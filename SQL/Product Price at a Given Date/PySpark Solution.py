from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Create Spark session
spark = SparkSession.builder \
    .appName("Last Prices") \
    .getOrCreate()

# Sample Products DataFrame
data = [
    (1, 100, '2019-08-01'),
    (1, 110, '2019-08-15'),
    (1, 105, '2019-08-17'),
    (2, 200, '2019-08-01'),
    (2, 210, '2019-08-05'),
    (3, 300, '2019-08-10'),
    (3, 290, '2019-08-12')
]

products_df = spark.createDataFrame(data, ['product_id', 'new_price', 'change_date'])

# Convert change_date to DateType
products_df = products_df.withColumn('change_date', F.to_date('change_date'))

# Filter products where change_date is less than or equal to '2019-08-16'
filtered_df = products_df.filter(products_df.change_date <= '2019-08-16')

# Create a window specification for ROW_NUMBER()
window_spec = Window.partitionBy('product_id').orderBy(F.desc('change_date'))

# Add row number to the filtered DataFrame
last_prices = filtered_df.withColumn('row_num', F.row_number().over(window_spec)) \
    .filter(F.col('row_num') == 1) \
    .select('product_id', 'new_price')

# Create the distinct product IDs DataFrame
dist_products = products_df.select('product_id').distinct()

# Perform the left join
result_df = dist_products.join(last_prices, on='product_id', how='left')

# Fill null values in new_price with 10
result_df = result_df.withColumn('price', F.coalesce(F.col('new_price'), F.lit(10)))

# Select the final columns
result_df = result_df.select('product_id', 'price')

result_df.show()
