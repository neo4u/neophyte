public class Solution {
    int[][] cache;
    public int calculateMinimumHP(int[][] dungeon) {
        cache = new int[dungeon.length][dungeon[0].length];
        int ret = search(dungeon, 0, 0);
        return ret > 0 ? 1 : -ret + 1;
    }
    private int search(int[][] matrix, int x, int y) {
        if (x == matrix.length - 1 && y == matrix[0].length - 1) return matrix[x][y] > 0 ? 0 : matrix[x][y];
        if (x < 0 || y < 0 || x >= matrix.length || y >= matrix[0].length) return Integer.MIN_VALUE;
        if (cache[x][y] != 0) return cache[x][y] == -1 ? 0 : cache[x][y];
        
        int left = search(matrix, x + 1, y);
        int right = search(matrix, x, y + 1);
        int cur = matrix[x][y] + Math.max(left, right);
        
        cache[x][y] = cur > 0 ? -1 : cur;
        return cur > 0 ? 0 : cur;
    }
}