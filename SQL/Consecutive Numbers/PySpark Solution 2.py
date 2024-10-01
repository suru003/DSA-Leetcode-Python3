from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

def find_consecutive_nums_spark(data):
    # Create a Spark session
    spark = SparkSession.builder.appName("Consecutive Numbers").getOrCreate()

    # Create DataFrame
    columns = ['id', 'num']
    df = spark.createDataFrame(data, columns)

    # Define a window specification to partition by nothing and order by 'id'
    window_spec = Window.orderBy('id')

    # Use lag() and lead() to create 'PrevNum' and 'NextNum' columns
    df = df.withColumn('PrevNum', F.lag('num', 1).over(window_spec)) \
           .withColumn('NextNum', F.lead('num', 1).over(window_spec))

    # Filter rows where 'num' is equal to both 'PrevNum' and 'NextNum'
    consecutive_nums_df = df.filter((df['num'] == df['PrevNum']) & (df['num'] == df['NextNum']))

    # Select distinct 'num' values and return the DataFrame
    distinct_consecutive_nums_df = consecutive_nums_df.select('num').distinct()
    return distinct_consecutive_nums_df

# Sample data
data = [(1, 1), (2, 1), (3, 1), (4, 2), (5, 2), (6, 2)]

# Call the function
result_df = find_consecutive_nums_spark(data)
result_df.show()
