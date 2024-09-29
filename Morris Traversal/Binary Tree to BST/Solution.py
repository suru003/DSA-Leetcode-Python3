"""
In interview

I was asked to convert a binary tree to a BST.
For my first approach, I explained taking the values into a vector, sorting them, and creating a new tree.

When asked to optimize for space, I suggested updating the tree's values in-place during an inorder traversal.

However, when asked to further optimize space , I was not able to further optimkse ,what would be the approach.

Can anyone share the optimised approach in terms of space and time complexity

Link: https://leetcode.com/discuss/interview-question/5844771/Amazon-6-months-SDE-Intern-2025-(JULY-2025-JAN-2026)
"""

# Time Complexity: O(nlogn)
# Space Complexity: O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to perform Morris Inorder Traversal and collect values
def morris_inorder_collect(root):
    current = root
    result = []

    while current:
        if current.left is None:
            result.append(current.data)  # Visit the node
            current = current.right
        else:
            # Find the inorder predecessor of current
            predecessor = current.left
            while predecessor.right is not None and predecessor.right != current:
                predecessor = predecessor.right

            # If right child of predecessor is None, set it to current
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                # Revert the changes made
                predecessor.right = None
                result.append(current.data)  # Visit the node
                current = current.right

    return result


# Function to perform Morris Inorder Traversal and update node values
def morris_inorder_update(root, sorted_values):
    current = root
    index = 0

    while current:
        if current.left is None:
            current.data = sorted_values[index]  # Update the node value
            index += 1
            current = current.right
        else:
            # Find the inorder predecessor of current
            predecessor = current.left
            while predecessor.right is not None and predecessor.right != current:
                predecessor = predecessor.right

            # If right child of predecessor is None, set it to current
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                # Revert the changes made
                predecessor.right = None
                current.data = sorted_values[index]  # Update the node value
                index += 1
                current = current.right


# Main function to convert a Binary Tree to a BST
def binary_tree_to_bst(root):
    # Step 1: Collect all node values using Morris Inorder Traversal
    values = morris_inorder_collect(root)

    # Step 2: Sort the values
    values.sort()

    # Step 3: Update the original tree in-place using Morris Inorder Traversal
    morris_inorder_update(root, values)


# Helper function to print the tree in inorder (for testing purposes)
def inorder_print(root):
    if root is None:
        return
    inorder_print(root.left)
    print(root.data, end=' ')
    inorder_print(root.right)


# Example usage
if __name__ == "__main__":
    # Create a sample binary tree
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)
    root.right.left = Node(1)
    root.right.left.left = Node(21)
    root.right.left.right = Node(2)

    print("Inorder traversal of original tree:")
    inorder_print(root)
    print("\n")

    # Convert binary tree to BST
    binary_tree_to_bst(root)

    print("Inorder traversal of converted BST:")
    inorder_print(root)
    print()
