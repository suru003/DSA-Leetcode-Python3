# https://leetcode.com/problems/product-sales-analysis-iii/
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Create a Spark session
spark = SparkSession.builder.appName("PySpark Example").getOrCreate()

# Sample Sales Data
data = [(1, 2020, 10, 100),
        (1, 2021, 15, 150),
        (2, 2019, 10, 200),
        (2, 2020, 5, 250),
        (3, 2022, 20, 300),
        (3, 2023, 25, 350)]

columns = ['product_id', 'year', 'quantity', 'price']

# Create DataFrame
sales_df = spark.createDataFrame(data, columns)

# Create the CTE equivalent
cte_df = sales_df.groupBy('product_id').agg(F.min('year').alias('minyear'))

# Join with the original Sales DataFrame
result_df = sales_df.join(cte_df, (sales_df['product_id'] == cte_df['product_id']) &
                           (sales_df['year'] == cte_df['minyear']))

# Select the relevant columns
final_result_df = result_df.select('product_id', 'year', 'quantity', 'price')

# Show the result
final_result_df.show()
