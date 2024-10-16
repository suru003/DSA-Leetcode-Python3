from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.sql.functions import col, row_number

# Create Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Sample DataFrame
data = [(1, 101, 0), (1, 102, 1), (2, 103, 0), (2, 104, 1), (3, 105, 1)]
df = spark.createDataFrame(data, ["employee_id", "department_id", "primary_flag"])

# Define window specification
window_spec = Window.partitionBy("employee_id").orderBy(col("primary_flag").desc())

# Apply row_number() function
df_with_rownum = df.withColumn("row_num", row_number().over(window_spec))

# Filter rows where row_num = 1
result_df = df_with_rownum.filter(col("row_num") == 1).select("employee_id", "department_id")

result_df.show()
