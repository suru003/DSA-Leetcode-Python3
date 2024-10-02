from pyspark.sql import functions as F

# Assuming 'df' is your DataFrame
df_filtered = df.filter((F.col('id') % 2 == 1) & (~F.col('description').rlike('boring')))
df_sorted = df_filtered.orderBy(F.col('rating').desc())

# Select the required columns
result = df_sorted.select('id', 'movie', 'description', 'rating')
result.show()
