# @param {String} path
# @return {String}
def simplify_path(path)
    simple_dirs = []
    dirs = path.split('/')
    dirs.each do |dir|
        next if dir == '.' || dir == ''
        if dir == '..'
            simple_dirs.pop unless simple_dirs.empty?
        else
            simple_dirs.push(dir)
        end
    end

    '/' + simple_dirs.join('/')
end

# 71.Simplify Path
# https://leetcode.com/problems/simplify-path/

# Time complexity: O(n).
# Space complexity: O(n), n is length of path.

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(simplify_path('/'), '/')
assert_equal(simplify_path('/...'), '/...')
assert_equal(simplify_path('/home/'), '/home')
assert_equal(simplify_path('/a/./b/../../c/'), '/c')
assert_equal(simplify_path("/."), '/')
assert_equal(simplify_path('/home//foo/'), '/home/foo')
