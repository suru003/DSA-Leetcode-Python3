import java.util.HashMap;
import java.util.Map;

class Solution {
    private static final int MOD = 1000000007;
    private int n;
    private String s;
    private Map<String, Integer> dp = new HashMap<>();

    public int countWinningSequences(String s) {
        this.n = s.length();
        this.s = s;
        return recurse(0, 0, ' ');
    }

    private int getScore(char bob, char alice) {
        if (bob == alice) return 0;
        if ((bob == 'F' && alice == 'E') || (bob == 'W' && alice == 'F') || (bob == 'E' && alice == 'W')) {
            return 1;
        }
        return -1;
    }

    private int recurse(int index, int score, char last) {
        if (score + n - index < 1) return 0;
        if (index == n) return 1;

        String key = index + "," + score + "," + last;
        if (dp.containsKey(key)) return dp.get(key);

        int total = 0;
        for (char current : new char[] { 'F', 'E', 'W' }) {
            if (current != last) {
                int dx = getScore(current, s.charAt(index));
                total = (total + recurse(index + 1, score + dx, current)) % MOD;
            }
        }

        dp.put(key, total);
        return total;
    }
}
