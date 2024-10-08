from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.sql.functions import col, lead, lag, when, coalesce

# Initialize Spark session
spark = SparkSession.builder.appName("StudentSwap").getOrCreate()

# Sample DataFrame
data = [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie'), (4, 'David'), (5, 'Eve')]
df = spark.createDataFrame(data, ['id', 'student'])

# Define the window specification
window_spec = Window.orderBy("id")

# Create lead and lag columns
df = df.withColumn("lead_student", lead("student").over(window_spec)) \
       .withColumn("lag_student", lag("student").over(window_spec))

# Apply the CASE WHEN logic
df = df.withColumn("student_swap", when(col("id") % 2 == 1, col("lead_student")).otherwise(col("lag_student")))

# Apply the COALESCE logic
df = df.withColumn("final_student", coalesce(col("student_swap"), col("student")))

# Select the final result
result = df.select("id", col("final_student").alias("student"))
result.show()
