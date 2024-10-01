# https://leetcode.com/problems/rising-temperature/
import pandas as pd

def rising_temperature(weather_df: pd.DataFrame) -> pd.DataFrame:
    # Create a shifted DataFrame with the 'recordDate' shifted by 1 day for comparison
    shifted_df = weather_df[['recordDate', 'temperature']].copy()
    shifted_df['recordDate'] = shifted_df['recordDate'] + pd.Timedelta(days=1)

    # Merge the original DataFrame with the shifted DataFrame on 'recordDate'
    merged_df = pd.merge(weather_df, shifted_df, on='recordDate', how='inner', suffixes=('', '_prev'))

    # Filter for records where the current temperature is greater than the previous day's temperature
    result_df = merged_df[merged_df['temperature'] > merged_df['temperature_prev']]

    result_df = result_df.drop(columns = ['recordDate', 'temperature', 'temperature_prev'])
    return result_df
