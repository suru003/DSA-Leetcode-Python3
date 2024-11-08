import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] getMaximumXor(int[] nums, int maximumBit) {
        List<Integer> answerList = new ArrayList<>();
        Integer current = null;

        int maxXor = (1 << maximumBit) - 1;

        for (int val : nums) {
            if (current != null) {
                current ^= val;
            } else {
                current = val;
            }

            String binary = Integer.toBinaryString(current);
            binary = "0".repeat(maximumBit - binary.length()) + binary;

            int currentAnswer = 0;
            for (int ind = 0; ind < maximumBit; ind++) {
                if (binary.charAt(ind) == '0') {
                    currentAnswer += 1 << (maximumBit - ind - 1);
                }
            }

            answerList.add(currentAnswer);
        }

        Collections.reverse(answerList);

        // Convert List<Integer> to int[]
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
    }
}
