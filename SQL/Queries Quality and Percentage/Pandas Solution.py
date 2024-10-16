# https://leetcode.com/problems/queries-quality-and-percentage/
import pandas as pd
from decimal import Decimal, ROUND_HALF_UP


# Custom rounding function
def round_half_up(value, digits):
    return float(Decimal(value).quantize(Decimal(f'1.{"0" * digits}'), rounding=ROUND_HALF_UP))


def queries_stats(queries_df: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Create a new column `quality_ratio`
    queries_df['quality_ratio'] = queries_df['rating'] / queries_df['position']

    # Step 2: Create the `is_poor` column based on condition (rating < 3)
    queries_df['is_poor'] = queries_df['rating'].apply(lambda x: 1 if x < 3 else 0)

    # Step 3: Group by `query_name` and calculate aggregated metrics
    result = queries_df.groupby('query_name').agg(
        quality=('quality_ratio', lambda x: round_half_up(x.mean(), 2)),
        poor_query_percentage=('is_poor', lambda x: round_half_up(x.mean() * 100, 2))).reset_index()

    return result
