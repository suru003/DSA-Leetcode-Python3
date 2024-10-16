from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Initialize Spark session
spark = SparkSession.builder.appName("triangle_check").getOrCreate()

# Sample DataFrame
data = [(3, 4, 5), (1, 1, 2), (5, 2, 3)]
columns = ["x", "y", "z"]
df = spark.createDataFrame(data, columns)

# Create a new column "triangle" with the condition logic
df = df.withColumn("triangle",
    when((col('x') + col('y') > col('z')) &
         (col('y') + col('z') > col('x')) &
         (col('x') + col('z') > col('y')), 'Yes')
    .otherwise('No')
)

# Show the result
df.show()
