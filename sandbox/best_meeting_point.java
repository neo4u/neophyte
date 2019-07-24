class Solution {
    public int minTotalDistance(int[][] grid) {
        List<Integer> rows = collectRows(grid);
        List<Integer> cols = collectCols(grid);
        int row = rows.get(rows.size() / 2);
        int col = cols.get(cols.size() / 2);
        return minDistance1D(rows, row) + minDistance1D(cols, col);
    }

    private int minDistance1D(List<Integer> points, int origin) {
        int distance = 0;
        for (int point : points) {
            distance += Math.abs(point - origin);
        }
        return distance;
    }

    private List<Integer> collectRows(int[][] grid) {
        List<Integer> rows = new ArrayList<>();
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {
                if (grid[row][col] == 1) {
                    rows.add(row);
                }
            }
        }
        return rows;
    }

    private List<Integer> collectCols(int[][] grid) {
        List<Integer> cols = new ArrayList<>();
        for (int col = 0; col < grid[0].length; col++) {
            for (int row = 0; row < grid.length; row++) {
                if (grid[row][col] == 1) {
                    cols.add(col);
                }
            }
        }
        return cols;
    }
}

// 296. Best Meeting Point
// https://leetcode.com/problems/best-meeting-point/description/

// Intuition:
// - Manhattan distance: (x1, y1), (x2, y2) is |x2 - x1| + |y2 - y2|
// - Manhattan distance means that we can travel only right angles as opposed to diagonal like in Eucledean distance
// - This means we can do the rows and take median and calculate the distance for all points to get to the median row
// - Then we can do the cols and take median and calcuate the distance for all points to get to the median col
// - Adding these two distances gives us the minDistance to get to the optimal point

// Question:
// For even number of houses can we choose a non-house point by
// taking average of middle two points in the sorted list of house points

// Time: O(mn)
// Space: O(mn)

