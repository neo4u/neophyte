# @param {Integer[][]} board
# @return {Void} Do not return anything, modify board in-place instead.
def game_of_life(board)
    m, n = board.size, board[0].size

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            count = live_neighbours(board, i, j)

            if board[i][j] == 0 # if dead
                board[i][j] = 2 if count == 3 # dead and 3 neighbours mark to bring to life
            else                # if alive
                board[i][j] = 3 if count < 2 || count > 3 # alive and <2 or >3 nbs make dead
            end
        end
    end

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            board[i][j] = 1 if board[i][j] == 2 # if 2 then make alive: 1
            board[i][j] = 0 if board[i][j] == 3 # if 3 then make dead: 0
        end
    end

    board # Remove return for submitting to LC's online judge, as they asked for inplace modification
end

def live_neighbours(board, i, j)
    count = 0
    nbs = [
        [0, 1], [1, 0], [1, -1], [1, 1],    # right, down, down left, down right
        [0, -1], [-1, 0], [-1, -1], [-1, 1] # left, up, up left, up right
    ]
    m, n = board.size, board[0].size
    nbs.each do |x1, y1|
        x, y = i + x1, j + y1
        next if !x.between?(0, m - 1) || !y.between?(0, n - 1) # skip if not in range
        count += board[x][y] % 2 # returns 1 for 1, 3, and 0 for 0, 2, Remember it could be either of 0, 1, 2, 3
    end

    count
end

# 289. Game of Life
# https://leetcode.com/problems/game-of-life/

# We denote:
# 2 to represent transition dead -> alive
# 3 to represent transition alive -> dead

# These are the possible states and conditions:
# Current State: Dead (0)
# Neighbours conditions:
# - < 2     -> remain dead
# - == 2    -> remain dead
# - == 3    -> make alive
# - > 3     -> remain dead

# Current State: Alive (1)
# Neighbours conditions:
# - < 2     -> make dead
# - == 2    -> remain alive
# - == 3    -> remain alive
# - > 3     -> make dead

# We only need to care about the following two conditions as they cause a switch of state:
# | State |live neighbrs | new value | change |
# |-------|--------------|-----------|--------|
# | alive | < 2 or > 3   | 3         | 1->0   |
# | dead  | == 3         | 2         | 0->1   |

# Steps:
# 1. Based on the above table, do a first pass to capture the transistions required
# 2. Based on the new transistions, do a second pass to finally store the next state

# Complexity
# Time: O(m * n)
# Space: O(1)

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

board = [[0,1,0],
         [0,0,1],
         [1,1,1],
         [0,0,0]]
next_state = [[0,0,0],
              [1,0,1],
              [0,1,1],
              [0,1,0]]
assert_equal(game_of_life(board), next_state)
