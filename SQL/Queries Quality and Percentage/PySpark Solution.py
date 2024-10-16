from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, avg, round, udf
from decimal import Decimal, ROUND_HALF_UP
from pyspark.sql.types import FloatType

# Initialize Spark session
spark = SparkSession.builder.appName('example').getOrCreate()

# Sample DataFrame (replace with your actual data)
data = [
    ('query1', 2.5, 1),
    ('query2', 4.0, 2),
    ('query3', 1.5, 1),
    ('query4', 3.5, 2)
]

# Creating a PySpark DataFrame
df = spark.createDataFrame(data, ['query_name', 'rating', 'position'])

# Step 1: Create the quality_ratio column
df = df.withColumn('quality_ratio', col('rating') / col('position'))

# Step 2: Create the is_poor column based on the condition (rating < 3)
df = df.withColumn('is_poor', when(col('rating') < 3, 1).otherwise(0))

# Custom round function using Decimal
def round_half_up(value, digits=2):
    return float(Decimal(value).quantize(Decimal(f'1.{"0" * digits}'), rounding=ROUND_HALF_UP))

# Create UDF for rounding
round_udf = udf(lambda x: round_half_up(float(x), 2), FloatType())

# Step 3: Group by query_name and calculate aggregated metrics
result = df.groupBy('query_name').agg(
    avg('quality_ratio').alias('quality'),
    (avg('is_poor') * 100).alias('poor_query_percentage')
)

# Apply UDF to DataFrame
result = result.withColumn('quality_ratio', round_udf(result['quality']))
result = result.withColumn('poor_query_percentage', round_udf(result['poor_query_percentage']))

result.show()
