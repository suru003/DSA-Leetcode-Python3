from pyspark.sql import SparkSession
from pyspark.sql.functions import split, expr, col

# Create Spark session
spark = SparkSession.builder.appName("Patients").getOrCreate()

# Example dataframe
data = [
    (1, 'John Doe', 'diab12 hypertension'),
    (2, 'Jane Smith', 'diab14 asthma'),
    (3, 'Sam Johnson', 'hypertension asthma')
]

df = spark.createDataFrame(data, ['patient_id', 'patient_name', 'conditions'])

# Split the 'conditions' column into an array of conditions
df = df.withColumn('condition_list', split(col('conditions'), ' '))

# Filter rows where any condition matches 'diab1%'
diabetes_pattern = '^diab1%'
filtered_df = df.withColumn('matched_condition', expr(f"filter(condition_list, x -> x ilike '{diabetes_pattern}')")) \
                .filter(expr("size(matched_condition) > 0"))

# Select relevant columns
result_df = filtered_df.select('patient_id', 'patient_name', 'conditions')

result_df.show(truncate=False)
