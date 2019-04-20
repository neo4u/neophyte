def missingWords(s, t)
    # Write your code here
    a = s.split()
    b = t.split()
    missing = []
    a.each do |w|
        if w == b.first
            b.shift()
        else
            missing.push(w)
        end
    end

    missing
end


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(
    missingWords(
        "I am using hackerrank to improve programming",
        "am hackerrank to improve"
    ),
    ["I",'using','programming']
)

assert_equal(
    missingWords(
        'Python is an easy to learn powerful programming language It has efficient high-level data structures and a simple but effective approach to objectoriented programming Python elegant syntax and dynamic typing',
        'Python is an easy to learn powerful programming language'
    ),
    ['It', 'has', 'efficient', 'high-level', 'data',
    'structures', 'and', 'a', 'simple', 'but',
    'effective', 'approach', 'to', 'objectoriented',
    'programming', 'Python', 'elegant',
    'syntax', 'and', 'dynamic', 'typing']
)
 