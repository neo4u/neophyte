def numberOfPatterns(self, m, n):
  """
  :type m: int
  :type n: int
  :rtype: int
  """
  # very clear java solution: https://discuss.leetcode.com/topic/46260/java-dfs-solution-with-clear-explanations-and-optimization-beats-97-61-12ms/2
  
  skip = [[0] * 10 for _ in range(10)]
  
  skip[1][3] = skip[3][1] = 2; 
  skip[1][7] = skip[7][1] = 4; 
  skip[7][9] = skip[9][7] = 8; 
  skip[3][9] = skip[9][3] = 6
  skip[1][9] = skip[9][1] = skip[7][3] = skip[3][7] = 5
  skip[2][8] = skip[8][2] = skip[4][6] = skip[6][4] = 5
  
  visited = [False] * 10
  
  def traverse(curr, remain_steps):
      if remain_steps == 0:
          return 1
      
      count = 0
      
      visited[curr] = True
      
      for i in range(1, 10):
          if not visited[i] and (skip[curr][i] == 0 or visited[skip[curr][i]]):
              count += traverse(i, remain_steps - 1)
      
      visited[curr] = False
      
      return count
  
  res = 0
  for i in range(m, n + 1):
      res += traverse(1, i - 1) * 4 # 1, 3, 7, 9 give same result
      res += traverse(2, i - 1) * 4 # 2, 4, 6, 8 give same result
      res += traverse(5, i - 1)
  
  return res