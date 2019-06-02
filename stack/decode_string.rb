def decode_string(s)
    stack, num = [["", 1]], ""

    s.each_char do |c|
        if is_digit?(c)
            num += c
        elsif is_alpha?(c)
            stack.last[0] += c
        elsif c == '['
            stack.push(["", num.to_i])
            num = ""
        elsif c == ']'
            str, k = stack.pop()
            stack.last[0] += str * k
        end
    end

    stack.first[0]
end

def is_alpha?(c)
    c.match(/[a-zA-Z]/)
end

def is_digit?(c)
    c.match(/[0-9]/)
end