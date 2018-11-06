# @param {Integer[]} tree
# @return {Integer}
def total_fruit(tree)
    ans, l, n, counter = 0, 0, tree.size, 0
    counts = Array.new(n, 0)

    tree.each_with_index do |x, r|
        counter += 1 if counts[x] == 0
        counts[x] += 1

        puts "tree type: #{x}, count: #{counts}"
        while counter >= 3
            puts "inside while"

            counts[tree[l]] -= 1
            counter -= 1 if counts[tree[l]] == 0
            puts "after kick #{counts}"
            l += 1
        end
        ans = [ans, r - l + 1].max
        puts "ans: #{ans}"
    end

    ans
end

# 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(total_fruit([3,3,3,1,2,1,1,2,3,3,4]), 5)
assert_equal(total_fruit([1,2,1]), 3)
assert_equal(total_fruit([0,1,2,2]), 3)
assert_equal(total_fruit([1,2,3,2,2]), 4)
