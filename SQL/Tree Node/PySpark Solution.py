from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col, lit

# Create a SparkSession
spark = SparkSession.builder.appName("Tree").getOrCreate()

# Sample DataFrame
data = [(1, None), (2, 1), (3, 1), (4, 2), (5, 3)]
columns = ["id", "p_id"]

df = spark.createDataFrame(data, columns)

# Identify parents (non-null p_id)
cte_parents = df.filter(col('p_id').isNotNull()).select(col('p_id')).distinct()

# Join the data to identify types (Root, Inner, Leaf)
result = df.withColumn(
    'type',
    when(col('p_id').isNull(), lit('Root'))  # Root condition
    .when(df['id'].isin([row['p_id'] for row in cte_parents.collect()]), lit('Inner'))  # Inner condition
    .otherwise(lit('Leaf'))  # Leaf condition
)

# Show the result
result.show()
