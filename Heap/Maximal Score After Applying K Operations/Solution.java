"""
Link: https://leetcode.com/problems/maximal-score-after-applying-k-operations/
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""
import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    public long maxKelements(int[] nums, int k) {
        // Using a max-heap (priority queue) where we negate numbers to simulate max-heap behavior
        PriorityQueue<Long> heap = new PriorityQueue<>(Collections.reverseOrder());

        // Insert all numbers as long into the heap
        for (int num : nums) {
            heap.add((long)num); // Cast num to long to avoid overflow
        }

        long answer = 0;

        while (k > 0) {
            // Remove the maximum element (heap root)
            long num = heap.poll();
            answer += num;

            // Perform the ceil division by 3 and push it back to the heap
            num = (long)Math.ceil((double)num / 3);
            heap.add(num);
            k--;
        }

        return answer;
    }
}
