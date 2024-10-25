public class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;
     TreeNode() {}
     TreeNode(int val) { this.val = val; }
     TreeNode(int val, TreeNode left, TreeNode right) {
         this.val = val;
         this.left = left;
         this.right = right;
     }
 }

class Solution {
    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        return dfs(root1, root2) && dfs(root2, root1);
    }

    private boolean dfs(TreeNode ptr1, TreeNode ptr2) {
        if ((ptr1 != null && ptr2 == null) || (ptr2 != null && ptr1 == null)) {
            return false;
        }
        if (ptr1 == null && ptr2 == null) {
            return true;
        }
        if (ptr1.val != ptr2.val) {
            return false;
        }

        boolean valid = true;

        if (ptr1.left != null) {
            if (ptr2.left != null && ptr2.left.val == ptr1.left.val) {
                valid &= dfs(ptr1.left, ptr2.left);
            } else if (ptr2.right != null && ptr2.right.val == ptr1.left.val) {
                valid &= dfs(ptr1.left, ptr2.right);
            } else {
                return false;
            }
        }

        if (ptr1.right != null) {
            if (ptr2.left != null && ptr2.left.val == ptr1.right.val) {
                valid &= dfs(ptr1.right, ptr2.left);
            } else if (ptr2.right != null && ptr2.right.val == ptr1.right.val) {
                valid &= dfs(ptr1.right, ptr2.right);
            } else {
                return false;
            }
        }

        return valid;
    }
}
