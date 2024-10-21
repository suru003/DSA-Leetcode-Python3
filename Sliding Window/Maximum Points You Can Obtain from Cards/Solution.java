class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        Map<Integer, Integer> counts = new HashMap<>();
        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            // Remove the element that is out of the sliding window
            if (i >= k) {
                counts.put(nums[i - k], counts.get(nums[i - k]) - 1);
                if (counts.get(nums[i - k]) == 0) {
                    counts.remove(nums[i - k]);
                }
            }

            // Add current element to the map
            counts.put(nums[i], counts.getOrDefault(nums[i], 0) + 1);

            // Once we have a full window, calculate the x most frequent sum
            if (i >= k - 1) {
                List<Map.Entry<Integer, Integer>> mostFreq = new ArrayList<>(counts.entrySet());

                // Sort by frequency and value
                mostFreq.sort((a, b) -> {
                    if (b.getValue().equals(a.getValue())) {
                        return b.getKey() - a.getKey(); // Sort by value in descending
                    } else {
                        return b.getValue() - a.getValue(); // Sort by frequency in descending
                    }
                });

                int tempSum = 0;
                for (int j = 0; j < Math.min(x, mostFreq.size()); j++) {
                    tempSum += mostFreq.get(j).getKey() * mostFreq.get(j).getValue();
                }

                answer.add(tempSum);
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}
