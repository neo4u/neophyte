// Logical Thought
// We aim to find all 'O's such that it is on the border or it is connected to an 'O' on the border.
// If we regard 'O' mentioned above as a node (or an element),
// the problem becomes to find the connected components (or disjoint sets) connected to borders.
// So-called borders should also be represented as an element,
// so elements connected to it can be merged with it into a set.
// That's the usage of dummyBorder.
// Pseudo-code

// initialize dummyRepresentative

// for O in board
// 	if O is on border
// 		union(dummyBorder, O)
// 	else
// 		for neighbour of O
// 			if (neighbour is 'O') 
// 				union(neighbour, O)
                
// for each cell
// 	if cell is 'O' && (find(cel) != find(dummyBorder))
// 		flip
// // Code

    private static int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};    
    public void solve(char[][] board) {
        
        if (board == null || board.length == 0) {
            return;
        }       
       
        DisjointSets disjointSets = new DisjointSets(board);
        int rows = board.length, cols = board[0].length;
        int dummyBorder = rows * cols;
        
        for (int x = 0; x < rows; x++) {
            for (int y = 0; y < cols; y++) {
                if (board[x][y] == 'O') {
                    int borderO = x * cols + y;
                    if (x == 0 || x == rows - 1 || y == 0 || y == cols - 1) {
                        disjointSets.union(dummyBorder, borderO);
                        continue;
                    }
                    for (int[] dir : directions) {
                        int nx = x + dir[0];
                        int ny = y + dir[1];
                        if (nx >= 0 && ny >= 0 && nx < rows && ny < cols && board[nx][ny] == 'O') {
                            int neighbor = nx * cols + ny;
                            disjointSets.union(borderO, neighbor);
                        }
                    }
                }
            }
        }
        
        for (int x = 0; x < rows; x++) {
            for (int y = 0; y < cols; y++) {
                if (board[x][y] == 'O' && disjointSets.find(x * cols + y) != disjointSets.find(dummyBorder)) {
                    board[x][y] = 'X';
                }
            }
        }
        
    }
    
    class DisjointSets {
        
        int[] parent;
        
        public DisjointSets(char[][] board) {
            
            int rows = board.length, cols = board[0].length;
            parent = new int[rows * cols + 1];
            
            for (int x = 0; x < rows; x++) {
                for (int y = 0; y < cols; y++) {       
                    if (board[x][y] == 'O') {
                        int id = x * cols + y;
                        parent[id] = id;
                    }
                }
            }
            parent[rows * cols] = rows * cols;
        }
        
        public int find(int x) {
            
            if (x == parent[x]) {
                return x;
            }
            return parent[x] = find(parent[x]);
        }
        
        public void union(int x, int y) {
            
            int rootX = find(x);
            int rootY = find(y);
            if (rootX != rootY) {
                parent[rootX] = rootY;
            }
        }
    }


// Trick

// We add an element dummyBorder to gather all elements connected to borders.
// I appreciate your VOTE UP (ˊo̴̶̷̤⌄o̴̶̷̤ˋ)