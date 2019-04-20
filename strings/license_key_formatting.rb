# @param {String} s
# @param {Integer} k
# @return {String}
def license_key_formatting(s, k)
    result, tmp = [], []
    (s.size - 1).downto(0) do |i|
        tmp.unshift(s[i].upcase) if alpha_num?(s[i])
        if tmp.size == k
            result.unshift(tmp.join(''))
            tmp = []
        end
    end
    result.unshift(tmp.join('')) if !tmp.empty?

    result.join('-')
end

def alpha_num?(str)
    str.match(/^[a-zA-Z0-9]$/)
end

def license_key_formatting_short(s, k)
    s.upcase.tr('-', '').reverse.scan(/.{1,#{k}}/).join('-').reverse
end




# 482. License Key Formatting
# https://leetcode.com/problems/license-key-formatting/description/


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(license_key_formatting("5F3Z-2e-9-w", 4), "5F3Z-2E9W")
assert_equal(license_key_formatting("2-4A0r7-4k", 4), "24A0-R74K")
