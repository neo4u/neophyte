class Solution {
	public int numIslands(char[][] grid) {
		if(grid == null || grid.length == 0 || grid[0].length == 0) return 0;
		int m = grid.length;
		int n = grid[0].length;
		int[] id = new int[m * n];
		int count = 0;

		for(int i = 0; i < m * n; i++) {
			id[i] = i;
		}

		for(int i = 0; i < m; i++) {
			for(int j = 0; j < n; j++) {
				if(grid[i][j] == '1') count++;
			}
		}

		for(int i = 0; i < m; i++) {
			for(int j = 0; j < n; j++) {
				if(grid[i][j] == '1') {
					if(connect(id, grid, i, j, i + 1, j)) count--;
					if(connect(id, grid, i, j, i - 1, j)) count--;
					if(connect(id, grid, i, j, i, j + 1)) count--;
					if(connect(id, grid, i, j, i, j - 1)) count--;
				}
			}
		}
		return count;
	}

	public boolean connect(int[] id, char[][] grid, int r1, int c1, int r2, int c2) {
		if(r2 < 0 || r2 >= grid.length || c2 < 0 || c2 >= grid[0].length || grid[r2][c2] != '1') return false;
		int id1 = r1 * grid[0].length + c1; 
		int id2 = r2 * grid[0].length + c2;
		int x = find(id, id1);
		int y = find(id, id2);
		if(x == y) return false;
		id[x] = y;
		return true;
	}

	public int find(int[] ids, int id) {
		if(ids[id] == id) return id;
		return find(ids, ids[id]);
	}
}