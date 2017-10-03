# @param {String} path
# @return {String}
def simplify_path(path)
  res_dirs = []
  dirs = path.split('/')
  dirs.each do |dir|
    next if dir == '.' || dir == '/' || dir == ''
    if dir == '..'
      res_dirs.pop unless res_dirs.empty?
    elsif dir.class == String
      res_dirs.push(dir)
    end
  end
  res_dirs.empty? ? res_dirs = ['', ''] : res_dirs.unshift('')

  res_dirs.join('/')
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(simplify_path('/'), '/')
assert_equal(simplify_path('/...'), '/...')
assert_equal(simplify_path('/home/'), '/home')
assert_equal(simplify_path('/a/./b/../../c/'), '/c')
assert_equal(simplify_path("/."), '/')
assert_equal(simplify_path('/home//foo/'), '/home/foo')
