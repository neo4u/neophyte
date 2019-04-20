# Complete the electionWinner function below.

import collections

def electionWinner(votes):
    map = collections.Counter(votes)
    return sorted(map.items(), key=lambda x: (x[1],x[0]))[-1][0]


assert electionWinner(['Alex', 'Michael', 'Harry', 'Dave', 'Michael', 'Victor', 'Harry', 'Alex', 'Mary', 'Mary']) == 'Michael'
assert electionWinner(['Victor','Veronica','Ryan','Dave','Maria','Maria','Farah','Farah','Ryan','Veronica']) == 'Veronica'
assert electionWinner(['Alice','Allison','Alice','Allison','Ashley','Ashley']) == 'Ashley'


