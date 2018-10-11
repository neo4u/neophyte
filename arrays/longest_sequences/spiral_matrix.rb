# @param {Integer[][]} matrix
# @return {Integer[]}
def spiral_order(matrix)
    result = []
    return result if !matrix || matrix.empty?

    r1, r2 = 0, matrix.size - 1
    c1, c2 = 0, matrix[0].size - 1

    while r1 <= r2 && c1 <= c2
        c1.upto(c2) { |c| result.push(matrix[r1][c]) }          # top border
        (r1 + 1).upto(r2) { |r| result.push(matrix[r][c2]) }    # right border

        if r1 < r2 && c1 < c2
            (c2 - 1).downto(c1 + 1) { |c| result.push(matrix[r2][c]) }
            r2.downto(r1 + 1) { |r| result.push(matrix[r][c1]) }
        end

        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
    end

    result
end

