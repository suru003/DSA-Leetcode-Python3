import java.util.HashSet;
import java.util.Set;

class Solution {
    private Set<String> words = new HashSet<>();

    public int maxUniqueSplit(String s) {
        return recurse(s, 0);
    }

    private int recurse(String s, int index) {
        int maxi = 0;
        for (int i = index + 1; i <= s.length(); i++) {
            String tempWord = s.substring(index, i);
            if (!words.contains(tempWord)) {
                words.add(tempWord);
                maxi = Math.max(maxi, 1 + recurse(s, i));
                words.remove(tempWord);
            }
        }
        return maxi;
    }
}
