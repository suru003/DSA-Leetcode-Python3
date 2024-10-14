import java.util.*;

class Solution {
    public int minGroups(int[][] intervals) {
        TreeMap<Integer, Integer> map = new TreeMap<>();

        // Populate the map with start and end points
        for (int[] interval : intervals) {
            int start = interval[0];
            int end = interval[1];

            map.put(start, map.getOrDefault(start, 0) + 1);
            map.put(end + 1, map.getOrDefault(end + 1, 0) - 1);
        }

        // Calculate max groups required
        int cur = 0, maxi = 0;
        for (int key : map.keySet()) {
            cur += map.get(key);
            maxi = Math.max(maxi, cur);
        }

        return maxi;
    }

}
