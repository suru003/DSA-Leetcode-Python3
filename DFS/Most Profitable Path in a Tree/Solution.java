class Solution {
    private Map<Integer, List<Integer>> graph;
    private int[] bobPath;
    private List<Integer> path;
    private int[] amount;

    public int mostProfitablePath(int[][] edges, int bob, int[] amount) {
        // Initialize class variables
        this.amount = amount;
        int nodes = amount.length;
        this.bobPath = new int[nodes];
        Arrays.fill(bobPath, -1);
        this.path = new ArrayList<>();
        path.add(bob);

        // Build the graph
        graph = new HashMap<>();
        for (int i = 0; i < nodes; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        // Fill Bob's path
        fillBobPath(bob, -1);

        // Fill bobPath array with time values
        for (int i = 0; i < path.size(); i++) {
            bobPath[path.get(i)] = i;
        }

        // Find Alice's maximum score
        return alicePath(0, -1, 0);
    }

    private boolean fillBobPath(int current, int parent) {
        if (current == 0) {
            return true;
        }

        for (int nbr : graph.get(current)) {
            if (nbr != parent) {
                path.add(nbr);
                if (fillBobPath(nbr, current)) {
                    return true;
                }
                path.remove(path.size() - 1);
            }
        }

        return false;
    }

    private int alicePath(int current, int parent, int currentTime) {
        int score = 0;

        if (bobPath[current] > currentTime || bobPath[current] == -1) {
            score = amount[current];
        } else if (bobPath[current] == currentTime) {
            score = amount[current] / 2;
        }

        int localMax = Integer.MIN_VALUE;
        boolean wentIn = false;

        for (int nbr : graph.get(current)) {
            if (nbr != parent) {
                wentIn = true;
                localMax = Math.max(localMax,
                    score + alicePath(nbr, current, currentTime + 1));
            }
        }

        return wentIn ? localMax : score;
    }
}