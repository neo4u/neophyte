# @param {String} word
# @param {String} abbr
# @return {Boolean}
def valid_word_abbreviation(word, abbr)
    i, j = 0, 0
    m, n = word.size, abbr.size

    while i < m && j < n
        while i < m && j < n && word[i] == abbr[j]
            i, j = i + 1, j + 1
        end
        return false if word[i] != abbr[j] && (!is_digit(abbr[j]) || abbr[j] == '0')

        cnt = 0
        while j < n && is_digit(abbr[j])
            cnt = cnt * 10 + abbr[j].to_i
            j += 1
        end

        i += cnt
    end

    i == m && j == n
end

def is_digit(c)
    c.between?('0', '9')
end


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(valid_word_abbreviation("internationalization", "i12iz4n"), true)
assert_equal(valid_word_abbreviation("apple", "a2e"), false)
assert_equal(valid_word_abbreviation("a", "1"), true)
assert_equal(valid_word_abbreviation("a", "2"), false)
assert_equal(valid_word_abbreviation("a", "01"), false)


