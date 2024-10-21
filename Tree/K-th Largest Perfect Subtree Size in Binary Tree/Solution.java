/**
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
import java.util.ArrayList;
import java.util.Collections;


class Solution {
    ArrayList<Integer> treeSizes = new ArrayList<>();

    // Helper method for recursion
    public int recurse(TreeNode current) {
        if (current == null) {
            return 0;
        }

        int left = recurse(current.left);
        int right = recurse(current.right);

        if (left != -1 && left == right) {
            treeSizes.add(left + right + 1);
            return left + right + 1;
        }

        return -1;
    }

    public int kthLargestPerfectSubtree(TreeNode root, int k) {
        // Start the recursion
        recurse(root);

        // Sort the sizes in ascending order
        Collections.sort(treeSizes);

        // Check if k is valid
        if (k > treeSizes.size()) {
            return -1;
        }

        // Return the kth largest size
        return treeSizes.get(treeSizes.size() - k);
    }
}
