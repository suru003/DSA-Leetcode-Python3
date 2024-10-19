import java.util.HashMap;
import java.util.Map;

class Solution {
    private Map<String, Integer> dp = new HashMap<>();
    private int maxi = 0;

    public int countMaxOrSubsets(int[] nums) {
        // Calculate maximum OR value for the nums array
        for (int val : nums) {
            maxi |= val;
        }
        // Call recursive function starting from index 0 and current OR value 0
        return recurse(0, 0, nums);
    }

    private int recurse(int index, int current, int[] nums) {
        String key = index + "," + current; // Generate unique key for memoization
        if (dp.containsKey(key)) {
            return dp.get(key);
        }

        if (index == nums.length) {
            return current == maxi ? 1 : 0;
        }

        // Option 1: Ignore current number
        int op1 = recurse(index + 1, current, nums);

        // Option 2: Use current number
        int op2 = recurse(index + 1, current | nums[index], nums);

        dp.put(key, op1 + op2);
        return op1 + op2;
    }

}
