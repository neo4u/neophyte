using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public int SnakesAndLadders(int[][] board)
    {
        int n = board.Length;
        int[] flatBoard = Flatten(board);

        int start = flatBoard[0] > -1 ? flatBoard[0] - 1 : 0;

        var q = new Queue<int>();
        q.Enqueue(start);

        var visited = new HashSet<int>();
        visited.Add(start);

        int steps = 0;
        while (q.Any())
        {
            int batchSize = q.Count;

            for (int x = 0; x < batchSize; x++)
            {
                int current = q.Dequeue();

                if (current == n * n - 1) return steps;

                for (int possibleNext = current + 1; possibleNext <= Math.Min(current + 6, n * n - 1); possibleNext++)
                {
                    int next = flatBoard[possibleNext] > -1 ? flatBoard[possibleNext] - 1 : possibleNext;

                    if (visited.Contains(next)) continue;

                    visited.Add(next);
                    q.Enqueue(next);
                }
            }

            steps++;
        }

        return -1;
    }

    private int[] Flatten(int[][] board)
    {
        int n = board.Length;
        var flatBoard = new int[n * n];

        int index = 0;
        bool rightToLeft = false;

        for (int row = n - 1; row >= 0; row--)
        {
            if (rightToLeft)
            {
                for (int col = board[row].Length - 1; col >= 0; col--)
                {
                    flatBoard[index] = board[row][col];
                    index++;
                }
            }
            else
            {
                for (int col = 0; col <= board[row].Length - 1; col++)
                {
                    flatBoard[index] = board[row][col];
                    index++;
                }
            }

            rightToLeft = !rightToLeft;
        }

        return flatBoard;
    }
}
