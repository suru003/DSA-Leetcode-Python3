from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, sum as spark_sum

# Create a Spark session
spark = SparkSession.builder.appName("CapitalGainLoss").getOrCreate()

# Sample DataFrame
data = [('AAPL', 'Buy', 150), ('AAPL', 'Sell', 200), ('TSLA', 'Buy', 300),
        ('TSLA', 'Sell', 350), ('GOOGL', 'Buy', 900), ('GOOGL', 'Sell', 850)]

columns = ['stock_name', 'operation', 'price']

df = spark.createDataFrame(data, columns)

# Perform the transformation
df = df.withColumn('capital_gain_loss',
                   when(col('operation') == 'Buy', -col('price')).otherwise(col('price')))

# Group by 'stock_name' and sum 'capital_gain_loss'
result = df.groupBy('stock_name').agg(spark_sum('capital_gain_loss').alias('capital_gain_loss'))

result.show()
