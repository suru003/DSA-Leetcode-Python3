import java.util.HashMap;
import java.util.Map;

class DSU {
    Map<Integer, Integer> parents;
    Map<Integer, Integer> sizes;

    public DSU() {
        parents = new HashMap<>();
        sizes = new HashMap<>();
    }

    public void addVal(int val) {
        parents.put(val, val);
        sizes.put(val, 1);
    }

    public int findParent(int val) {
        if (parents.get(val) == val) {
            return val;
        }
        int root = findParent(parents.get(val));
        parents.put(val, root);
        return root;
    }

    public void union(int a, int b) {
        int parentA = findParent(a);
        int parentB = findParent(b);

        if (parentA != parentB) {
            if (parentA >= parentB) {
                parents.put(parentB, parentA);
                sizes.put(parentA, sizes.get(parentA) + sizes.get(parentB));
            } else {
                parents.put(parentA, parentB);
                sizes.put(parentB, sizes.get(parentB) + sizes.get(parentA));
            }
        }
    }

    public int maxSize() {
        return sizes.values().stream().max(Integer::compare).orElse(1);
    }
}

public class Solution {
    public int longestSquareStreak(int[] nums) {
        DSU dsu = new DSU();
        for (int val : nums) {
            dsu.addVal(val);
        }

        for (int val : nums) {
            int next = val * val;
            dsu.findParent(val);

            if (dsu.parents.containsKey(next)) {
                dsu.union(val, next);
            }
        }

        int answer = dsu.maxSize();
        return answer == 1 ? -1 : answer;
    }
}
