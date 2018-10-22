# @param {String} s
# @param {Integer} k
# @return {String}
def license_key_formatting(s, k)
    result, tmp = [], []
    (s.size - 1).downto(0) do |i|
        tmp.unshift(s[i].upcase) if alpha_num?(s[i].upcase)
        if tmp.size == k
            result.unshift(tmp.join(''))
            tmp = []
        end
    end
    result.unshift(tmp.join('')) if !tmp.empty?

    result.join('-')
end

def alpha_num?(c)
    c.between?('A', 'Z') || c.between?('0', '9')
end

def license_key_formatting_short(s, k)
    s.upcase.tr('-', '').reverse.scan(/.{1,#{k}}/).join('-').reverse
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(license_key_formatting("5F3Z-2e-9-w", 4), "5F3Z-2E9W")
assert_equal(license_key_formatting("2-4A0r7-4k", 4), "24A0-R74K")
