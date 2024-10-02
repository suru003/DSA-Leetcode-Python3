# https://leetcode.com/problems/count-salary-categories/
import pandas as pd

def count_salary_categories(accounts_df: pd.DataFrame) -> pd.DataFrame:
    # High Salary
    high_salary_count = len(accounts_df[accounts_df['income'] > 50000])

    # Low Salary
    low_salary_count = len(accounts_df[accounts_df['income'] < 20000])

    # Average Salary
    average_salary_count = len(accounts_df[(accounts_df['income'] >= 20000) & (accounts_df['income'] <= 50000)])

    # Combine results
    result_df = pd.DataFrame({
        'category': ['High Salary', 'Low Salary', 'Average Salary'],
        'accounts_count': [high_salary_count, low_salary_count, average_salary_count]
    })

    return result_df
