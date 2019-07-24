# @param {Integer} n
# @param {Integer} k
# @return {Integer[][]}
def combine(n, k)
    return [] if n == 0 || k == 0
    bt(1, n, k)
end

def bt(first_num, n, k, path = [], result = [])
    return result.push(path) if path.size == k

    first_num.upto(n) do |i|
        bt(i + 1, n, k, path + [i], result)
    end

    result
end


require 'test/unit'
extend Test::Unit::Assertions

# Input:    4, 2
# Expected: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

assert_equal(combine(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])

# bt(1, 4, [])
#     bt(2, [1])
#         bt(3, [1, 2])
#         ret
#         bt(4, [1, 3])
#         ret
#         bt(5, [1, 4])
#         ret
#     ret
#     bt(3, [2])
#         bt(4, [2, 3])
#         ret
#         bt(5, [2, 4])
#         ret
#     ret
#     bt(4, [3])
#         bt(5, [3, 4])
#         ret
#     ret
#     bt(5, [4])
#     ret
# ret



def combine(n, k)
    return [[]] if k == 0 || n == 0

    prevs = combine(n - 1, k - 1)
    res = []

    prevs.each do |prev|
        start = prev.empty? ? 1 : prev.last + 1
        start.upto(n) do |i|
            res.push(prev + [i])
        end
    end

    res
end




# c(4,2)
#     c(3,1)
#         c(2,0)
#         return [[]]
#     return [[1], [2], [3], [4]]
# return [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

# [1,2,3,4] = > res([1,2,3]) + f(4)

# [1] => [1,2], [1,3], [1,4]
# [2] => [2,3], [2,4]
# [3] => [3,4]




       

# [1,2,3],  [1,2,4], [1,3,4], [2,3,4]