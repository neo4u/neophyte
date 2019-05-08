using System;

public class TicTacToe
{
    private int[] rows;
    private int[] cols;
    private int size;
    private int diagonal;
    private int antiDiagonal;

    /** Initialize your data structure here. */
    public TicTacToe(int n)
    {
        rows = new int[n];
        cols = new int[n];
        size = n;
    }

    public int Move(int row, int col, int player)
    {
        int score = player == 1 ? 1 : -1;

        rows[row] += score;
        cols[col] += score;

        if (row == col) diagonal += score;
        if (row + col == size - 1) antiDiagonal += score;
        if (Math.Abs(rows[row]) == size || Math.Abs(cols[col]) == size || Math.Abs(diagonal) == size || Math.Abs(antiDiagonal) == size) return player;
        return 0;
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.Move(row,col,player);
 */
