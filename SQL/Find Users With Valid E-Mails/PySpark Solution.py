from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Initialize SparkSession
spark = SparkSession.builder.appName("MailFilter").getOrCreate()

# Sample Data
data = [("user1@leetcode.com",), ("user2@otherdomain.com",), ("test.leetcode@leetcode.com",)]
columns = ["mail"]

# Creating DataFrame
df = spark.createDataFrame(data, columns)

# Applying the filter using rlike
filtered_df = df.filter(F.col("mail").rlike(r'^[a-zA-Z]+[a-zA-Z0-9_.-]*@leetcode\.com$'))

# Show the filtered DataFrame
filtered_df.show()
