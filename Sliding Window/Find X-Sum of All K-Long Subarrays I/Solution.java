import java.util.HashMap;
import java.util.Map;

class Solution {
    // Function to calculate current value from the bits map
    int getValue(Map<Integer, Integer> setBits) {
        int curVal = 0;
        for (Map.Entry<Integer, Integer> entry : setBits.entrySet()) {
            if (entry.getValue() > 0) {
                curVal += (1 << entry.getKey());
            }
        }
        return curVal;
    }

    public int minimumSubarrayLength(int[] nums, int k) {
        Map<Integer, Integer> setBits = new HashMap<>();
        int n = nums.length;
        int curVal = 0;
        int answer = n + 1;
        int i = 0, j = 0;

        if (k == 0) {
            return 1;
        }

        while (j < n) {
            // move right pointer
            while (j < n && curVal < k) {
                curVal |= nums[j];
                String binary = new StringBuilder(Integer.toBinaryString(nums[j])).reverse().toString();

                for (int index = 0; index < binary.length(); index++) {
                    if (binary.charAt(index) == '1') {
                        setBits.put(index, setBits.getOrDefault(index, 0) + 1);
                    }
                }
                j++;
            }

            // move left pointer
            while (i < n && curVal >= k) {
                answer = Math.min(answer, j - i);

                String binary = new StringBuilder(Integer.toBinaryString(nums[i])).reverse().toString();

                for (int index = 0; index < binary.length(); index++) {
                    if (binary.charAt(index) == '1') {
                        setBits.put(index, setBits.getOrDefault(index, 0) - 1);
                    }
                }
                curVal = getValue(setBits);
                i++;
            }
        }

        return (answer == n + 1) ? -1 : answer;
    }
}
