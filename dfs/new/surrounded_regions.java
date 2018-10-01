// Logical Thinking
// We aim to set all O's which doesn't locate at borders or connect to O at borders to X.
// We mark all O's at borders and apply DFS at each O at boarders to mark all O's connected to it.
// The un-marked O's ought to be set X.

// Trick
// We search for invalid candidates (and exclude them) rather than search for valid candidates.

// Code

    boolean[][] visited;
    
    public void solve(char[][] board) {
        
        if (board == null || board.length == 0 || board[0].length == 0) {
            return;
        }
        
        int rows = board.length, cols = board[0].length;
        visited = new boolean[rows][cols];
        
        for (int i = 0; i < rows; i++) {
            
            if (board[i][0] == 'O' && !visited[i][0]) {
                detectConnected(i, 0, board);
            }
            
            if (board[i][cols - 1] == 'O' && !visited[i][cols - 1]) {
                detectConnected(i, cols - 1, board);
            }
        }
        for (int j = 0; j < cols; j++) {
            
            if (board[0][j] == 'O' && !visited[0][j]) {
                detectConnected(0, j, board);
            }
            
            if (board[rows - 1][j] == 'O' && !visited[rows - 1][j]) {
                detectConnected(rows - 1, j, board);
            }
        }
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == 'O' && !visited[i][j]) {
                    board[i][j] = 'X';
                }
            }
        }
    }
    
    private void detectConnected(int x, int y, char[][] board) {
        
        if (x < 0 || x >= board.length || y < 0 || y >= board[0].length || visited[x][y] || board[x][y] != 'O') {
            return;
        }
        
        visited[x][y] = true;
        
        detectConnected(x + 1, y, board);
        detectConnected(x, y + 1, board);
        detectConnected(x - 1, y, board);
        detectConnected(x, y - 1, board);
    }


// I appreciate your VOTE UP (ˊo̴̶̷̤⌄o̴̶̷̤ˋ)