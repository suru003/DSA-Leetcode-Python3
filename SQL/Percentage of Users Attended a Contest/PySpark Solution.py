from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Initialize Spark session
spark = SparkSession.builder.appName("ContestPercentage").getOrCreate()

# Sample data for users and Register
users_df = spark.createDataFrame([(1,), (2,), (3,), (4,), (5,)], ['user_id'])  # Example users table
register_df = spark.createDataFrame([
    (101,), (102,), (101,), (103,), (101,), (102,), (103,), (104,), (102,), (104,)
], ['contest_id'])  # Example Register table

# Step 1: Calculate the total number of users
total_users = users_df.count()

# Step 2: Aggregate by contest_id and calculate percentage
agg_df = register_df.groupBy('contest_id').agg(F.count('*').alias('count'))
agg_df = agg_df.withColumn('percentage', F.round((agg_df['count'] / total_users) * 100, 2))

# Step 3: Sort the result
agg_df = agg_df.orderBy(agg_df['percentage'].desc(), agg_df['contest_id'].asc())

# Output
agg_df.show()
