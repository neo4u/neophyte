# @param {Character[][]} board
# @return {Void} Do not return anything, modify board in-place instead.
def solve_sudoku(board)
    @board = board
    solve()
end

def check_row(r, n)
    0.upto(8) do |c|
        return false if @board[r][c] == n
    end

    true
end

def check_col(c, n)
    0.upto(8) do |r|
        return false if @board[r][c] == n
    end

    true
end

def check_square(r, c, n)
    r.upto(r + 2) do |row|
        c.upto(c + 2) do |col|
            return false if @board[row][col] == n
        end
    end

    true
end

def safe?(r, c, n)
    box_r = r - r%3
    box_c = c - c%3
    return true if check_row(r, n) && check_col(c, n) && check_square(box_r, box_c, n)

    false
end

def find_unassigned()
    0.upto(8) do |r|
        0.upto(8) do |c|
            return [r, c] if @board[r][c] == '.'
        end
    end

    [-1, -1]
end

def solve()
    r, c = find_unassigned()
    return true if r == -1 && c == -1 # no more unassigned, puzzle solved!

    '1'.upto('9') do |n|
        next if !safe?(r, c, n)  # Check if this n is safe in position [r, c]
        @board[r][c] = n        # Mark that position with safe number and go deeper
        return true if solve()  # Go as deep as possible for current solution
        @board[r][c] = '.'      # If we haven't returned true then, current [r, c] doesn't work, so bt
    end

    false
end

# 37. Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/description/

require 'test/unit'
extend Test::Unit::Assertions

board = [['5','3','.','.','7','.','.','.','.'],
         ['6','.','.','1','9','5','.','.','.'],
         ['.','9','8','.','.','.','.','6','.'],
         ['8','.','.','.','6','.','.','.','3'],
         ['4','.','.','8','.','3','.','.','1'],
         ['7','.','.','.','2','.','.','.','6'],
         ['.','6','.','.','.','.','2','8','.'],
         ['.','.','.','4','1','9','.','.','5'],
         ['.','.','.','.','8','.','.','7','9']]
solved = [['5','3','4','6','7','8','9','1','2'],
          ['6','7','2','1','9','5','3','4','8'],
          ['1','9','8','3','4','2','5','6','7'],
          ['8','5','9','7','6','1','4','2','3'],
          ['4','2','6','8','5','3','7','9','1'],
          ['7','1','3','9','2','4','8','5','6'],
          ['9','6','1','5','3','7','2','8','4'],
          ['2','8','7','4','1','9','6','3','5'],
          ['3','4','5','2','8','6','1','7','9']]
solve_sudoku(board)
assert_equal(board, solved)
