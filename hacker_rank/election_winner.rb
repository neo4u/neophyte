# Complete the electionWinner function below.
def electionWinner(votes)
    map = {}
    votes.each do |n|
        map[n] = map.fetch(n, 0) + 1
    end
    map.sort_by(&:reverse)&.last[0]
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(electionWinner(['Alex', 'Michael', 'Harry', 'Dave', 'Michael', 'Victor', 'Harry', 'Alex', 'Mary', 'Mary']), 'Michael')
assert_equal(electionWinner(['Victor','Veronica','Ryan','Dave','Maria','Maria','Farah','Farah','Ryan','Veronica']), 'Veronica')
assert_equal(electionWinner(['Alice','Allison','Alice','Allison','Ashley','Ashley']), 'Ashley')
