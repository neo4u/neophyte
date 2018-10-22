# @param {Integer} x
# @return {Integer}
def reverse(x)
    x = x < 0 ? -reverse_int(-x) : reverse_int(x)
    x.between?(-2**31, 2**31 - 1) ? x : 0
end

def reverse_int(x)
    reversed = 0
    until x.zero?
        reversed = reversed * 10 + x % 10
        x /= 10
    end

    reversed
end

# Easier way
# def reverse()
#   x = x < 0 ? -((-x).to_s.chars.reverse.join.to_i) : x.to_s.chars.reverse.join.to_i
# end

puts reverse(-123)
