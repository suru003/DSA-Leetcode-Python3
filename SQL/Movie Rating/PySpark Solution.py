from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, month, year

# Assuming movie_rating, users, and movies are DataFrames loaded into Spark

# Step 1: Calculate the top user by the number of movie ratings
top_user = movie_rating.join(users, movie_rating.user_id == users.user_id, 'inner') \
                       .groupBy(users.name) \
                       .agg(count("*").alias("rating_count")) \
                       .orderBy(col("rating_count").desc(), users.name.asc()) \
                       .limit(1) \
                       .select(users.name.alias("results"))

# Step 2: Calculate the top movie rated in February 2020 by average rating
top_movie = movie_rating.filter((month(col("created_at")) == 2) & (year(col("created_at")) == 2020)) \
                        .join(movies, movie_rating.movie_id == movies.movie_id, 'inner') \
                        .groupBy(movies.title) \
                        .agg(avg(col("rating")).alias("avg_rating")) \
                        .orderBy(col("avg_rating").desc(), movies.title.asc()) \
                        .limit(1) \
                        .select(movies.title.alias("results"))

# Step 3: Union the top user and top movie results
result = top_user.union(top_movie)

# Show the result
result.show()
