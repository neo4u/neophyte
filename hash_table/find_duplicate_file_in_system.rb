# @param {String[]} paths
# @return {String[][]}
def find_duplicate(paths)
    map = Hash.new { |h, k| h[k] = [] }

    paths.each do |str|
        root, *files = str.split()
        files.each do |file|
            name, _, data = file.partition('(')
            map[data[0, data.size - 1]].push("#{root}/#{name}")
        end
    end

    map.values.select { |files| files.length > 1 }
end

# 609. Find Duplicate File in System
# https://leetcode.com/problems/find-duplicate-file-in-system/

# After parsing, we have some path and content.
# Let's store a map M[content] = [path1, path2, ...].
# At the end, we want all values in this map with length > 1.

# n strings of avg. length x
# Time: O(n * x)
# Space: O(n * x)