# @param {String} s
# @return {Boolean}
def valid_palindrome(s)
  l, r = 0, s.size - 1
  while l < r
    if s[l] != s[r]
      s1, s2 = s[l..r - 1], s[l + 1..r]
      return s1 == s1.reverse || s2 == s2.reverse
    end
    l, r = l + 1, r - 1
  end

  true
end
