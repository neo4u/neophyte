require 'set'

# TLE Solution, bcuz only counts are needed. Not the actual paths.
# Also, hacky in the sense of eliminating duplicate paths using sort on curr_path @$$)(Q@)#(*#)
# @param {Integer[]} coins
# @param {Integer} amount
# @return {Integer}
def change(amount, coins)
    return 0 if amount.zero?
    paths = []

    q, visited = [[0, []]], Set.new([])
    while !q.empty?
        node, path = q.shift
        coins.each do |coin|
            nxt_node = coin + node
            curr_path = path + [coin]

            if nxt_node == amount
                puts "nxt_node: #{nxt_node}, path: #{curr_path}, sorted path: #{curr_path.sort}, visited: #{visited}"
                paths.push(curr_path.sort) if !visited.include?(curr_path.sort)
                visited.add(curr_path.sort) # Only way to keep 
                next
            end
            next if visited.include?(curr_path.sort)
            next if nxt_node > amount

            visited.add(curr_path.sort)
            q.push([nxt_node, curr_path])
        end
    end

    p paths
    paths.count
end


# 322. Coin Change
# https://leetcode.com/problems/coin-change/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(change(5, [1,2, 5]), 4)