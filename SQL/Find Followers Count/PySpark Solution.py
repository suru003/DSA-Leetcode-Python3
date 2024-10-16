from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Initialize Spark session
spark = SparkSession.builder.appName("FollowersCount").getOrCreate()

# Sample data representing Followers table
data = [(1,), (2,), (1,), (3,), (2,), (3,), (3,)]
columns = ['user_id']

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Group by user_id and count the number of followers
followers_count_df = df.groupBy('user_id').agg(count('*').alias('followers_count'))

# Sort by user_id
followers_count_df = followers_count_df.orderBy(col('user_id'))

# Show the result
followers_count_df.show()
