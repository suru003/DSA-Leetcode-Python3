from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, when, col

# Create Spark session
spark = SparkSession.builder.appName("TransactionSum").getOrCreate()

# Sample Data
data = [
    ('2024-09-24', 15),
    ('2024-09-24', 20),
    ('2024-09-25', 30),
    ('2024-09-25', 7)
]

# Create DataFrame
df = spark.createDataFrame(data, ['transaction_date', 'amount'])

# Create odd_sum and even_sum
df_with_sums = df.withColumn('odd_sum', when(col('amount') % 2 == 1, col('amount')).otherwise(0)) \
    .withColumn('even_sum', when(col('amount') % 2 == 0, col('amount')).otherwise(0))

# Group by transaction_date and calculate sums
result = df_with_sums.groupBy('transaction_date') \
    .agg(sum('odd_sum').alias('odd_sum'), sum('even_sum').alias('even_sum')) \
    .orderBy('transaction_date')

# Show result
result.show()
