from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, when, avg, round
from pyspark.sql.types import StringType

# Initialize Spark session
spark = SparkSession.builder.appName("TripCancellationRate").getOrCreate()

# Sample DataFrames
users_data = [(1, 'no'), (2, 'yes'), (3, 'no'), (4, 'no')]
users_df = spark.createDataFrame(users_data, ["users_id", "banned"])

trips_data = [
    (1, 3, 'cancelled', '2013-10-01'),
    (2, 4, 'completed', '2013-10-02'),
    (3, 2, 'cancelled', '2013-10-03'),
    (1, 1, 'completed', '2013-10-02')
]
trips_df = spark.createDataFrame(trips_data, ["client_id", "driver_id", "status", "request_at"])

# Step 1: Filter valid users who are not banned
valid_users_df = users_df.filter(lower(col('banned')) == 'no').select('users_id')

# Step 2: Filter trips within date range and where both client and driver are valid
filtered_trips_df = trips_df.filter(
    (col('request_at') >= '2013-10-01') &
    (col('request_at') <= '2013-10-03') &
    (col('client_id').isin([row.users_id for row in valid_users_df.collect()])) &
    (col('driver_id').isin([row.users_id for row in valid_users_df.collect()]))
)

# Step 3: Calculate the cancellation flag
filtered_trips_df = filtered_trips_df.withColumn(
    'cancellation', when(lower(col('status')).like('%cancelled%'), 1).otherwise(0)
)

# Step 4: Group by 'request_at' (Day) and calculate average cancellation rate
cancellation_rate_df = filtered_trips_df.groupBy('request_at').agg(
    round(avg(col('cancellation')), 2).alias('Cancellation Rate')
)

# Final result
cancellation_rate_df.show()
