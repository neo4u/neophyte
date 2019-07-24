using System;
using System.Collections.Generic;

public class Solution
{
    public void SolveSudoku(char[][] board)
    {
        if (board == null || board.Length == 0) return;

        var visited = new HashSet<string>();
        BuildVisited(board, visited);
        Solve(board, visited);
    }

    private void BuildVisited(char[][] board, HashSet<string> visited)
    {
        for (int row = 0; row < board.Length; row++)
        {
            for (int col = 0; col < board[row].Length; col++)
            {
                char ch = board[row][col];
                if (ch != '.')
                {
                    AddVisited(row, col, ch, visited);
                }
            }
        }
    }

    private bool Solve(char[][] board, HashSet<string> visited)
    {
        for (int row = 0; row < board.Length; row++)
        {
            for (int col = 0; col < board[row].Length; col++)
            {
                char ch = board[row][col];
                if (ch != '.')
                {
                    continue;
                }

                for (char c = '1'; c <= '9'; c++)
                {
                    if (!IsValid(board, row, col, c, visited))
                    {
                        continue;
                    }

                    board[row][col] = c;
                    AddVisited(row, col, c, visited);
                    if (Solve(board, visited)) return true;
                    board[row][col] = ch;
                    RemoveVisited(row, col, c, visited);
                }
                return false;
            }
        }
        return true;
    }

    private void RemoveVisited(int row, int col, char c, HashSet<string> visited)
    {
        visited.Remove("row" + row + ":" + c);
        visited.Remove("col" + col + ":" + c);
        visited.Remove("block" + row / 3 + "-" + col / 3 + ":" + c);
    }

    private void AddVisited(int row, int col, char c, HashSet<string> visited)
    {
        visited.Add("row" + row + ":" + c);
        visited.Add("col" + col + ":" + c);
        visited.Add("block" + row / 3 + "-" + col / 3 + ":" + c);
    }

    private bool IsValid(char[][] board, int row, int col, char c, HashSet<string> visited)
    {
        return !visited.Contains("row" + row + ":" + c) && !visited.Contains("col" + col + ":" + c) && !visited.Contains("block" + row / 3 + "-" + col / 3 + ":" + c);
    }
}