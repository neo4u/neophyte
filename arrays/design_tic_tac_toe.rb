class TicTacToe
    def initialize(n)
        @rows = Array.new(n, 0)
        @cols = Array.new(n, 0)
        @diag = 0
        @anti_diag = 0
        @size = n
    end

    def move(row, col, player)
        to_add = player == 1 ? 1 : -1

        @rows[row] += to_add
        @cols[col] += to_add
        @diag += to_add if row == col
        @anti_diag += to_add if row + col == @size - 1

        return player if [
            @rows[row].abs,
            @cols[col].abs,
            @diag.abs,
            @anti_diag.abs
        ].include?(@size)

        0
    end
end

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe.new(n)
# param_1 = obj.move(row, col, player)