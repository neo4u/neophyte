import java.util.HashMap;
import java.util.PriorityQueue;

class EightPuzzleAssist implements Comparable<EightPuzzleAssist> {
    public int[][] board;
    public int row;
    public int col;
    public int gn;
    public int hn;
    public int fn;
    public EightPuzzleAssist(int[][] board, int row, int col, int gn, int hn) {
        super();
        this.board = board;
        this.row = row;
        this.col = col;
        this.gn = gn;
        this.hn = hn;
        this.fn = gn + hn;
    }
    @Override
    public int compareTo(EightPuzzleAssist o) {
        return this.fn - o.fn;
    }

}
public class Solution {
    private final int[] dRow = {0, 0, -1, 1};
    private final int[] dCol = {1, -1, 0, 0};
    private final int[][] target = {{1, 2, 3}, {4, 5, 0}};
    private int M = 2;
    private int N = 3;
    public int slidingPuzzle(int[][] board) {
        int nixuCnt = getNixu(board);
        if ((nixuCnt & 1) != 0) {
            return -1;
        }
        PriorityQueue<EightPuzzleAssist> queue = new PriorityQueue<EightPuzzleAssist>();
        HashMap<String, EightPuzzleAssist> set = new HashMap<String, EightPuzzleAssist>();
        int[] startIndex = getZeroIndex(board);
        queue.offer(new EightPuzzleAssist(deepClone(board), startIndex[0],
                startIndex[1], 0, computeHn(board)));
        set.put(boardToHashKey(board), queue.peek());

        while (!queue.isEmpty()) {
            EightPuzzleAssist p = queue.poll();

            if (p.hn == 0) {
                return p.gn;
            } else {
                for (int i = 0; i < dRow.length; i++) {
                    if (checkIndexBounds(p.row + dRow[i], p.col + dCol[i])) {
                        int[][] matrix = deepClone(p.board);

                        swap(matrix, p.row, p.col, p.row + dRow[i], p.col + dCol[i]);
                        String key = boardToHashKey(matrix);
                        int childHn = computeHn(matrix);
                        if (!set.containsKey(key)) {
                            EightPuzzleAssist child = new EightPuzzleAssist(
                                    matrix, p.row + dRow[i], p.col + dCol[i],
                                    p.gn + 1, childHn);
                            queue.offer(child);
                            set.put(key, child);
                        }
                    }
                }
            }
        }
        return -1;
    }

    private void swap(int[][] board, int row1, int col1, int row2, int col2) {
        int t = board[row1][col1];
        board[row1][col1] = board[row2][col2];
        board[row2][col2] = t;
    }

    private int[][] deepClone(int[][] board) {
        int[][] matrix = new int[M][N];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                matrix[i][j] = board[i][j];
            }
        }
        return matrix;
    }

    private int[] getZeroIndex(int[][] board) {
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 0) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[2];
    }

    private int getNixu(int[][] board) {
        int[] array = new int[M * N - 1];
        int index = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] != 0) {
                    array[index] = board[i][j];
                    index++;
                }
            }
        }
        int cnt = 0;
        for (int i = 0; i < array.length - 1; i++) {
            for (int j = i + 1; j < array.length; j++) {
                if (array[i] > array[j]) {
                    cnt++;
                }
            }
        }
        return cnt;
    }

    private int computeHn(int[][] board) {
        int cnt = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] != target[i][j]) {
                    cnt++;
                }
            }
        }
        return cnt;
    }

    private String boardToHashKey(int[][] board) {
        String str = "";
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                str += board[i][j] + "_";
            }
        }
        return str;
    }

    private boolean checkIndexBounds(int row, int col) {
        if (row >= 0 && row < M && col >= 0 && col < N) {
            return true;
        } else {
            return false;
        }
    }
}
