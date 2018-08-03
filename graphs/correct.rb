# @param {Integer[][]} grid
# @return {Integer}
def max_area_of_island(grid)
	m, n = grid.count, grid[0].count
	return 0 if grid.empty?
	max_area = 0

	0.upto(m - 1) do |r|
		0.upto(n - 1) do |c|
			if grid[r][c] == 1
				@area = 0
				dfs(grid,r,c)
				max_area = @area if @area > max_area
			end
		end
	end

	max_area
end

def dfs(grid, r, c)
	return if grid[r][c] == 0

	@size += 1
	grid[r][c] = 0
	dfs(grid,r+1,c) if r < grid.count-1
	dfs(grid,r-1,c) if r > 0
	dfs(grid,r,c+1) if c < grid[0].count-1
	dfs(grid,r,c-1) if c > 0
end