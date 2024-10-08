from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Initialize Spark session
spark = SparkSession.builder.appName("RollingWindowExample").getOrCreate()

# Sample data for the Customer table
data = [
    ('2024-01-01', 100),
    ('2024-01-02', 150),
    ('2024-01-03', 200),
    ('2024-01-04', 250),
    ('2024-01-05', 300),
    ('2024-01-06', 350),
    ('2024-01-07', 400),
    ('2024-01-08', 450),
    ('2024-01-09', 500),
    ('2024-01-10', 550)
]
columns = ['visited_on', 'amount']

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Define the window for the last 7 days (inclusive of the current day)
windowSpec = Window.orderBy("visited_on").rowsBetween(-6, 0)

# Calculate rolling sum and average
df_with_rolling = df.withColumn("rolling_sum", F.sum("amount").over(windowSpec)) \
                    .withColumn("rolling_avg", F.round(F.avg("amount").over(windowSpec), 2))

# Apply OFFSET equivalent by filtering the first 6 rows
df_result = df_with_rolling.orderBy("visited_on").limit(10).filter(F.row_number().over(Window.orderBy("visited_on")) > 6)

# Show result
df_result.show()
