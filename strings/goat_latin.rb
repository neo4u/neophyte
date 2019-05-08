# @param {String} s
# @return {String}
def to_goat_latin(s)
    vowels = Set.new('aeiouAEIOU'.chars)
    result = ''

    s.split(" ").each_with_index do |word, i|
        c = word[0]
        new_word = (vowels.include?(c) ? word : word[1...word.size] + c) + 'ma' + 'a' * (i + 1)
        result += (result.empty? ? '' : ' ') + new_word
    end

   result
end

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(
    to_goat_latin("The quick brown fox jumped over the lazy dog"),
    "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
)
