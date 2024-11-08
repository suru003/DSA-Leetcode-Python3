class Solution {
    int getOnes(int num) {
            return Integer.bitCount(num);
        }

    public boolean canSortArray(int[] nums) {
        int i = 0, n = nums.length;
        int prevMax = 0;


        while (i < n) {
            int windowOnes = getOnes(nums[i]);
            int mini = nums[i], maxi = nums[i];

            int j = i + 1;
            while (j < n && getOnes(nums[j]) == windowOnes) {
                mini = Math.min(mini, nums[j]);
                maxi = Math.max(maxi, nums[j]);
                j++;
            }

            if (mini < prevMax) {
                return false;
            }

            prevMax = maxi;
            i = j;
        }

        return true;
    }
}
