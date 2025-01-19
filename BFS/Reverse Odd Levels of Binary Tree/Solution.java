import java.util.*;
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

class Solution {
    public TreeNode reverseOddLevels(TreeNode root) {
        Queue<Object[]> queue = new LinkedList<>();
        queue.add(new Object[]{Collections.singletonList(root), true});

        while (!queue.isEmpty()) {
            Object[] pair = queue.poll();
            List<TreeNode> level = (List<TreeNode>) pair[0];
            boolean flag = (boolean) pair[1];

            List<TreeNode> nextLevel = new ArrayList<>();

            for (TreeNode node : level) {
                if (node.left != null) {
                    nextLevel.add(node.left);
                }
                if (node.right != null) {
                    nextLevel.add(node.right);
                }
            }

            if (flag) {
                for (int i = 0; i < nextLevel.size() / 2; i++) {
                    TreeNode left = nextLevel.get(i);
                    TreeNode right = nextLevel.get(nextLevel.size() - 1 - i);
                    int temp = left.val;
                    left.val = right.val;
                    right.val = temp;
                }
            }

            if (!nextLevel.isEmpty()) {
                queue.add(new Object[]{nextLevel, !flag});
            }
        }

        return root;
    }
}
