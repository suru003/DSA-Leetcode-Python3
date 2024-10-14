"""
Link: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""

import java.util.*;

public class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        List<int[]> numsInds = new ArrayList<>();
        int indLength = nums.size();

        // Flatten the nums array with indices
        for (int ind = 0; ind < indLength; ind++) {
            for (int val : nums.get(ind)) {
                numsInds.add(new int[]{val, ind});
            }
        }

        // Sort numsInds by the value (first element of each pair)
        numsInds.sort(Comparator.comparingInt(a -> a[0]));

        int numsIndsLen = numsInds.size();
        int i = 0, j = 0;
        int[] counts = new int[indLength];
        int nonZeroes = 0;
        int minRange = numsInds.get(numsIndsLen - 1)[0] - numsInds.get(0)[0];
        int[] answerRange = {numsInds.get(0)[0], numsInds.get(numsIndsLen - 1)[0]};

        while (j < numsIndsLen) {
            while (j < numsIndsLen && nonZeroes != indLength) {
                int[] valInd = numsInds.get(j);
                int val = valInd[0], ind = valInd[1];

                if (counts[ind] == 0) {
                    nonZeroes++;
                }

                counts[ind]++;
                j++;
            }

            while (i < j && nonZeroes == indLength) {
                int a = numsInds.get(i)[0], ind_i = numsInds.get(i)[1];
                int b = numsInds.get(j - 1)[0];

                int tempRange = b - a;
                if (tempRange < minRange) {
                    minRange = tempRange;
                    answerRange = new int[]{a, b};
                }

                counts[ind_i]--;
                if (counts[ind_i] == 0) {
                    nonZeroes--;
                }

                i++;
            }
        }

        return answerRange;
    }
}
