impl Solution {
    pub fn sort_matrix(mut grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();

        // Sort diagonals starting from the last row
        for row in (0..m).rev() {
            let mut temp_list = Vec::new();
            let (mut x, mut y) = (row, 0);
            while x < m && y < n {
                temp_list.push(grid[x][y]);
                x += 1;
                y += 1;
            }

            temp_list.sort_by(|a, b| b.cmp(a)); // Sort in descending order
            let mut index = 0;
            let (mut x, mut y) = (row, 0);
            while x < m && y < n {
                grid[x][y] = temp_list[index];
                x += 1;
                y += 1;
                index += 1;
            }
        }

        // Sort diagonals starting from the last column
        for col in (1..n).rev() {
            let mut temp_list = Vec::new();
            let (mut x, mut y) = (0, col);
            while x < m && y < n {
                temp_list.push(grid[x][y]);
                x += 1;
                y += 1;
            }

            temp_list.sort(); // Sort in ascending order
            let mut index = 0;
            let (mut x, mut y) = (0, col);
            while x < m && y < n {
                grid[x][y] = temp_list[index];
                x += 1;
                y += 1;
                index += 1;
            }
        }

        grid
    }
}