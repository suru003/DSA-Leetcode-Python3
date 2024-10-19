import java.util.ArrayList;
import java.util.List;

class Solution {
    public char findKthBit(int n, int k) {
        n -= 1;
        List<Character> bits = new ArrayList<>();
        bits.add('0');

        for (int i = 1; i <= n; i++) {
            int prevLength = bits.size();
            bits.add('1');

            for (int curIndex = prevLength - 1; curIndex >= 0; curIndex--) {
                bits.add(bits.get(curIndex) == '1' ? '0' : '1');
            }
        }

        return bits.get(k - 1);
    }
}
