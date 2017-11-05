# @note This solution is a little slow but easy to understand. The faster solution is to save indexes of start and end of longest palindrome
# @param {String} s
# @return {String}
def longest_palindrome(s)
  res, n = "", s.size
  0.upto(n - 1) do |i|
    res = [get_longest_palin(s, i, i), get_longest_palin(s, i, i + 1), res].max_by(&:size)
  end

  res
end

def get_longest_palin(s, l, r)
  while 0 <= l && r < s.size && s[l] == s[r]
    l -= 1
    r += 1
  end
  s[(l + 1)...r]
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(longest_palindrome("babad"), "aba")
assert_equal(longest_palindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"), "ranynar")

# FASTEST SOLUTION
# def longest_palindrome(s)
#   return "" if s.length < 1
#   head, n = 0, s.size
#   maxlen = 1
#   0.upto(n - 1) do |i|
#     if i - maxlen >= 1 && s[(i - maxlen - 1)..i] == s[(i - maxlen - 1)..i].reverse
#       head = i - maxlen - 1
#       maxlen += 2
#     end
#     if i - maxlen >= 0 && s[(i - maxlen)..i] == s[(i - maxlen)..i].reverse
#       head = i - maxlen
#       maxlen += 1
#     end
#   end
#   s[head..(head + maxlen - 1)]
# end
