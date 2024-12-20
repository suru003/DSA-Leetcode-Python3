import java.util.Arrays;

class Solution {
    // Custom binary search function
    int customBisectRight(int[][] items, int query) {
        int left = 0, right = items.length;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (items[mid][0] <= query) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    public int[] maximumBeauty(int[][] items, int[] queries) {
        // Sort items by price
        Arrays.sort(items, (a, b) -> Integer.compare(a[0], b[0]));

        // Generate the max beauty array
        int[] maxi = new int[items.length + 1];
        for (int i = 0; i < items.length; i++) {
            maxi[i + 1] = Math.max(maxi[i], items[i][1]);
        }

        // Process each query
        int[] answer = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int index = customBisectRight(items, queries[i]);
            answer[i] = maxi[index];
        }

        return answer;
    }
}
