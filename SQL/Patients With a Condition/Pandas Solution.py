# https://leetcode.com/problems/patients-with-a-condition/
import pandas as pd

def find_patients(patients_df: pd.DataFrame) -> pd.DataFrame:
    # Split the 'conditions' column into a list of conditions
    patients_df['condition_list'] = patients_df['conditions'].str.split()

    # Filter rows where any condition matches the regex pattern
    diabetes_pattern = '^diab1.*'
    filtered_df = patients_df[patients_df['condition_list']\
                    .apply(lambda x: any(pd.Series(x).str.contains(diabetes_pattern, case=False)))]

    # Select relevant columns
    result_df = filtered_df[['patient_id', 'patient_name', 'conditions']]

    return result_df
