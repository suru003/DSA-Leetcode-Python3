from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct

# Create Spark session
spark = SparkSession.builder.appName('example').getOrCreate()

# Sample Data
data = [
    (1, 101),
    (1, 102),
    (2, 101),
    (2, 103),
    (3, 102),
    (3, 102),
    (3, 104)
]

# Create DataFrame
columns = ['teacher_id', 'subject_id']
df = spark.createDataFrame(data, columns)

# Group by teacher_id and count distinct subject_id
result = df.groupBy('teacher_id').agg(countDistinct('subject_id').alias('cnt'))

result.show()
