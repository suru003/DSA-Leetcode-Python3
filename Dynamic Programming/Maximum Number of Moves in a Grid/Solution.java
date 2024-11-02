import java.util.HashMap;
import java.util.Map;

class Solution {
    private Map<String, Integer> dp = new HashMap<>();
    private int[][] adj = {{-1, 1}, {0, 1}, {1, 1}};
    private int m, n;

    public int maxMoves(int[][] grid) {
        m = grid.length;
        n = grid[0].length;
        int ans = 0;

        for (int i = 0; i < m; i++) {
            ans = Math.max(recurse(i, 0, grid), ans);
        }

        return ans;
    }

    private int recurse(int i, int j, int[][] grid) {
        String key = i + "," + j;
        if (dp.containsKey(key)) {
            return dp.get(key);
        }

        int nextMoves = 0;
        for (int[] direction : adj) {
            int newI = i + direction[0];
            int newJ = j + direction[1];

            if (newI >= 0 && newI < m && newJ >= 0 && newJ < n && grid[newI][newJ] > grid[i][j]) {
                nextMoves = Math.max(nextMoves, 1 + recurse(newI, newJ, grid));
            }
        }

        dp.put(key, nextMoves);
        return nextMoves;
    }
}
