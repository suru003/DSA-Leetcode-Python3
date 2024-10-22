import java.util.*;

/*
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    public long kthLargestLevelSum(TreeNode root, int k) {
        // Deque to hold the levels of the tree
        Queue<List<TreeNode>> dq = new LinkedList<>();
        dq.offer(Arrays.asList(root));
        // List to store the sum of each level
        List<Long> sums = new ArrayList<>();

        // Perform a level-order traversal
        while (!dq.isEmpty()) {
            List<TreeNode> currentLevel = dq.poll();
            List<TreeNode> nextLevel = new ArrayList<>();
            long curSum = 0;  // Use long to handle large sums

            // For each node in the current level, calculate the sum and prepare the next level
            for (TreeNode node : currentLevel) {
                curSum += node.val;  // Accumulate the sum
                if (node.left != null) {
                    nextLevel.add(node.left);
                }
                if (node.right != null) {
                    nextLevel.add(node.right);
                }
            }

            // Add the current level sum to the list
            sums.add(curSum);
            // If there are nodes in the next level, add them to the deque
            if (!nextLevel.isEmpty()) {
                dq.offer(nextLevel);
            }
        }

        // Sort the sums in descending order
        sums.sort(Collections.reverseOrder());
        // Return the k-th largest sum if it exists, otherwise return -1
        return sums.size() < k ? -1 : sums.get(k - 1);
    }
}
