from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Create Spark Session
spark = SparkSession.builder.appName("request_counts").getOrCreate()

# Sample DataFrame
data = [(1, 2), (2, 3), (1, 2), (3, 1), (2, 1), (3, 1)]
df = spark.createDataFrame(data, ["requester_id", "accepter_id"])

# Step 1: Count occurrences of 'requester_id'
requester_counts = df.groupBy("requester_id").count()

# Step 2: Count occurrences of 'accepter_id'
accepter_counts = df.groupBy("accepter_id").count().withColumnRenamed("accepter_id", "requester_id")

# Step 3: Union the two counts
combined_counts = requester_counts.unionByName(accepter_counts)

# Step 4: Group by 'requester_id' and sum the counts
final_result = combined_counts.groupBy("requester_id").agg(F.sum("count").alias("num"))

# Step 5: Sort by the sum and get the top result
top_result = final_result.orderBy(F.desc("num")).limit(1)

top_result.show()
