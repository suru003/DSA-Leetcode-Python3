# https://leetcode.com/problems/last-person-to-fit-in-the-bus/
import pandas as pd


def last_passenger(queue_df: pd.DataFrame) -> pd.DataFrame:
    # Step 0: Sort the values based on `turn`
    queue_df = queue_df.sort_values(by='turn', ascending=True)

    # Step 1: Calculate the cumulative sum of weights
    queue_df['cumm_sum'] = queue_df['weight'].cumsum()

    # Step 2: Filter where cumulative sum is less than or equal to 1000
    filtered_df = queue_df[queue_df['cumm_sum'] <= 1000]

    # Step 3: Sort by cumulative sum in descending order and get the first entry
    result = filtered_df.sort_values(by='cumm_sum', ascending=False).head(1)

    # Extracting the person_name
    person_name = result['person_name'].values[0]

    return pd.DataFrame({'person_name': [person_name]})
