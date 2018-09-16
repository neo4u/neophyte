# @param {String} s
# @return {String}
def longest_palindrome(s)
    longest, n = '', s.size

    0.upto(n - 1) do |i|
        longest = [
            get_longest_palindrome(s, i, i),     # Case of Odd length palindromes
            get_longest_palindrome(s, i, i + 1), # Case of Even length palindromes
            longest
        ].max_by(&:size)
    end

    longest
end

def get_longest_palindrome(s, l, r)
    while 0 <= l && r < s.size && s[l] == s[r]
        l -= 1; r += 1
    end

    s[l + 1...r]
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(longest_palindrome("a"), "a")
assert_equal(longest_palindrome("ccc"), "ccc")
assert_equal(longest_palindrome("babad"), "aba")
assert_equal(longest_palindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"), "ranynar")
