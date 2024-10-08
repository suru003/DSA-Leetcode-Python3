# https://leetcode.com/problems/exchange-seats/
import pandas as pd

def exchange_seats(seat_df: pd.DataFrame) -> pd.DataFrame:
    # Create a copy for shifting operations
    seat_df['lead_student'] = seat_df['student'].shift(-1)  # Equivalent to LEAD
    seat_df['lag_student'] = seat_df['student'].shift(1)    # Equivalent to LAG

    # Apply the CASE WHEN logic
    seat_df['student_swap'] = seat_df.apply(lambda row: row['lead_student'] if row['id'] % 2 == 1 else row['lag_student'], axis=1)

    # Final result with COALESCE equivalent
    seat_df['final_student'] = seat_df['student_swap'].combine_first(seat_df['student'])

    # Select the final result
    result = seat_df[['id', 'final_student']].rename(columns={'final_student': 'student'})
    return result
