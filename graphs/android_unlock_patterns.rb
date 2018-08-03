# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def number_of_patterns(m, n)
  @skip = Array.new(10) { [-1] * 10 }

  # Set skip nodes where skip[u][v] is the node to skip to connect u to v
  @skip[1][3] = @skip[3][1] = 2
  @skip[1][7] = @skip[7][1] = 4
  @skip[7][9] = @skip[9][7] = 8
  @skip[3][9] = @skip[9][3] = 6
  @skip[1][9] = @skip[9][1] = @skip[7][3] = @skip[3][7] = 5
  @skip[2][8] = @skip[8][2] = @skip[4][6] = @skip[6][4] = 5

  visited, result = [false] * 10, 0

  m.upto(n) do |len|
    # Pass len - 1 to symbolize reduction of path length by 1 for current node
    result += dfs(1, len - 1, visited) * 4 # 1, 3, 7, 9 gives same count
    result += dfs(2, len - 1, visited) * 4 # 2, 4, 6, 8 gives same count
    result += dfs(5, len - 1, visited)
  end

  result
end

def dfs(u, len, visited)
  return 1 if len.zero?
  count, visited[u] = 0, true

  # 1. Ensure v is not visited
  # 2. Ensure that either there is no skip node
  # or
  # 3. if skip node exists it is already visited.
  1.upto(9) do |v|
    count += dfs(v, len - 1, visited) if !visited[v] && (@skip[u][v] == -1 || visited[@skip[u][v]])
  end
  visited[u] = false # reset visited for next pattern
  count
end

