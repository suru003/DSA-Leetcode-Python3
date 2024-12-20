class Solution {
    public boolean canChange(String start, String target) {
        int n = start.length();
        int startPtr = 0;
        int targetPtr = 0;

        while (targetPtr < n) {
            while (targetPtr < n && target.charAt(targetPtr) == '_') {
                targetPtr++;
            }

            while (startPtr < n && start.charAt(startPtr) == '_') {
                startPtr++;
            }

            if (startPtr < n && targetPtr < n) {
                if (target.charAt(targetPtr) != start.charAt(startPtr)) {
                    return false;
                }

                if (target.charAt(targetPtr) == 'L' && startPtr < targetPtr) {
                    return false;
                }

                if (target.charAt(targetPtr) == 'R' && startPtr > targetPtr) {
                    return false;
                }
            }

            startPtr++;
            targetPtr++;
        }

        return countChar(start, 'L') == countChar(target, 'L')
            && countChar(start, 'R') == countChar(target, 'R');
    }

    private int countChar(String s, char ch) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == ch) {
                count++;
            }
        }
        return count;
    }
}
