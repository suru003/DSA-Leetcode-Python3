# https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Count occurrences of 'requester_id'
    requester_counts = request_accepted.groupby('requester_id').size().reset_index(name='count')

    # Step 2: Count occurrences of 'accepter_id'
    accepter_counts = request_accepted.groupby('accepter_id').size().reset_index(name='count')
    accepter_counts.rename(columns={'accepter_id': 'requester_id'}, inplace=True)

    # Step 3: Union the two counts
    combined_counts = pd.concat([requester_counts, accepter_counts], axis=0)

    # Step 4: Group by 'requester_id' and sum the counts
    final_result = combined_counts.groupby('requester_id').sum().reset_index()

    # Step 5: Sort by the sum and get the top result
    top_result = final_result.sort_values('count', ascending=False).head(1)

    top_result.rename(columns = {"requester_id": "id", "count": "num"}, inplace = True)
    return top_result
