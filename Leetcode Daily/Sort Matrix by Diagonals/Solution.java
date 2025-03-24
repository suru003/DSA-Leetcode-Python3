// https://leetcode.com/problems/sort-matrix-by-diagonals/description/

class Solution {
    public int[][] sortMatrix(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int x, y, index;

        for(int row = m - 1; row >= 0; row--) {
            ArrayList<Integer> tempList = new ArrayList<>();
            x = row;
            y = 0;

            while(x < m && y < n) {
                tempList.add(grid[x][y]);
                x++;
                y++;
            }

            Collections.sort(tempList, Collections.reverseOrder());
            x = row;
            y = 0;
            index = 0;

            while(x < m && y < n) {
                grid[x][y] = tempList.get(index);
                x++;
                y++;
                index++;
            }
        }

        for(int col = n - 1; col > 0; col--) {
            ArrayList<Integer> tempList = new ArrayList<>();
            x = 0;
            y = col;

            while(x < m && y < n) {
                tempList.add(grid[x][y]);
                x++;
                y++;
            }

            Collections.sort(tempList);
            x = 0;
            y = col;
            index = 0;

            while(x < m && y < n) {
                grid[x][y] = tempList.get(index);
                x++;
                y++;
                index++;
            }
        }

        return grid;
    }
}