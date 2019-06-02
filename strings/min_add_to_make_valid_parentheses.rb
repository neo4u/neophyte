# @param {String} s
# @return {Integer}
def min_add_to_make_valid(s)
    open, invalid_close = 0, 0

    s.each_char do |paren|
        if paren == "("
            open += 1
        else
            open > 0 ? open -= 1 : invalid_close += 1
        end
    end

    invalid_close + open
end

# Faster ruby specific version
# @param {String} s
# @return {Integer}
def min_add_to_make_valid(s)
    while s.include?("()")
        s.gsub!("()", "")
    end

    return s.size
end

# 921. Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
