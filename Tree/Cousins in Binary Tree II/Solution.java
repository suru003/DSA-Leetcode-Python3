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
    public TreeNode replaceValueInTree(TreeNode root) {
        Queue<List<List<TreeNode>>> queue = new LinkedList<>();
        queue.add(Arrays.asList(Arrays.asList(root)));

        while (!queue.isEmpty()) {
            List<List<TreeNode>> currentLevel = queue.poll();
            int total = 0;

            // Calculate the total sum of values at this level
            for (List<TreeNode> siblings: currentLevel) {
                for (TreeNode node: siblings) {
                    total += node.val;
                }
            }

            List<List<TreeNode>> nextLevel = new ArrayList<>();

            for (List<TreeNode> siblings: currentLevel) {
                int siblingsTotal = 0;
                for (TreeNode node: siblings) {
                    siblingsTotal += node.val;
                }

                for (TreeNode node: siblings) {
                    // Prepare the list of children nodes for the next level
                    List<TreeNode> children = new ArrayList<>();

                    // Update the node's value
                    node.val = total - siblingsTotal;

                    if (node.left != null)
                        children.add(node.left);

                    if (node.right != null)
                        children.add(node.right);

                    if (!children.isEmpty()) {
                        nextLevel.add(children);
                    }
                }
            }

            // Add next level nodes to the queue
            if (!nextLevel.isEmpty()) {
                queue.add(nextLevel);
            }
        }

        return root;
    }
}
