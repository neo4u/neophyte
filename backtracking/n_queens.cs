using System;
using System.Collections.Generic;
using System.Text;

public class Solution
{
    public IList<IList<string>> SolveNQueens(int n)
    {
        var result = new List<IList<string>>();
        var board = new char[n, n];

        for (int row = 0; row < board.GetLength(0); row++)
        {
            for (int col = 0; col < board.GetLength(1); col++)
            {
                board[row, col] = '.';
            }
        }

        SolveNQueensR(board, 0, result, n);
        return result;
    }

    private void SolveNQueensR(char[,] board, int row, List<IList<string>> result, int n)
    {
        if (row == n)
        {
            List<string> res = GetResult(board);
            result.Add(res);
            return;
        }

        for (int col = 0; col < n; col++)
        {
            if (IsValid(board, row, col))
            {
                board[row, col] = 'Q';
                SolveNQueensR(board, row + 1, result, n);
                board[row, col] = '.';
            }
        }
    }

    private List<string> GetResult(char[,] board)
    {
        var res = new List<string>();

        for (int row = 0; row < board.GetLength(0); row++)
        {
            var sb = new StringBuilder();

            for (int col = 0; col < board.GetLength(1); col++)
            {
                sb.Append(board[row, col]);
            }

            res.Add(sb.ToString());
        }

        return res;
    }

    private bool IsValid(char[,] board, int row, int col)
    {
        // check column of all previous rows
        for (int r = 0; r < row; r++)
        {
            if (board[r, col] == 'Q') return false;
        }

        // check left diagonal
        for (int r = row - 1, c = col - 1; r >= 0 && c >= 0; r--, c--)
        {
            if (board[r, c] == 'Q') return false;
        }

        // check right diagonal
        for (int r = row - 1, c = col + 1; r >= 0 && c < board.GetLength(1); r--, c++)
        {
            if (board[r, c] == 'Q') return false;
        }

        return true;
    }
}