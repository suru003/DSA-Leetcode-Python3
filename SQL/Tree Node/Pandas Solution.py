# https://leetcode.com/problems/tree-node/
import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    # Identify the parents (non-null p_id values)
    parents = tree[tree['p_id'].notnull()]['p_id']

    # Apply the conditions using the apply function
    tree['type'] = tree.apply(lambda row: 'Root' if pd.isnull(row['p_id'])
                        else 'Inner' if row['id'] in parents.values
                        else 'Leaf', axis=1)

    return tree[['id', 'type']]
