import collections
import itertools
from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        m = collections.defaultdict(int)

        for t in transactions:
            m[t[0]] -= t[2]
            m[t[1]] += t[2]

        debt = m.values()
        return self.bt(0, debt)

    def bt(self, s_idx, debt):
        while s_idx < len(debt) and debt[s_idx] == 0: s_idx += 1
        if s_idx == len(debt): return 0
        result = float('inf')

        for i in range(s_idx + 1, len(debt)):
            if debt[i] * debt[s_idx] < 0:
                # settle s with i
                debt[i] += debt[s_idx]
                result = min(result, 1 + self.bt(s_idx + 1, debt))
                # backtrack
                debt[i] -= debt[s_idx]

        return result


# https://leetcode.com/problems/optimal-account-balancing/discuss/95355/Concise-9ms-DFS-solution-(detailed-explanation)


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        ledger = collections.defaultdict(int) #key: person add value

        for t in transactions:
            ledger[t[0]] -= t[2]
            ledger[t[1]] += t[2]

        return self.bt({k:v for k, v in ledger.items() if v})

    def bt(self, balance):
        if not balance: return 0
        n = len(balance)

        for group_size in range(2, n + 1):
            for keys in itertools.combinations(balance.keys(), group_size):
                if sum(balance[k] for k in keys) == 0:
                    s = set(keys)
                    return group_size - 1 + self.bt({k: v for k, v in balance.items() if k not in s})


class Solution(object):
    def minTransfers(self, transactions):
        self.ledger = collections.defaultdict(int)
        people = set()

        for giver, receiver, amount in transactions:
            self.ledger[giver] -= amount
            self.ledger[receiver] += amount
            people |= {giver, receiver}

        ledger = {k:v for k, v in self.ledger.items() if v}
        people_list = list(ledger.keys())

        return self.dfs(people_list)

    def dfs(self, people_list):
        if not people_list: return 0

        people, n = set(people_list), len(people_list)
        for i in range(2, n + 1):
            for persons in itertools.combinations(people_list, i):
                if sum(self.ledger[p] for p in persons) == 0:
                    people -= set(persons)
                    return self.dfs(list(people)) + len(persons) - 1



class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        d = collections.Counter()
        for t in transactions:
            d[t[0]] += t[2]
            d[t[1]] -= t[2]

        balances = [d[person] for person in d if d[person] != 0]
        # balances = list(filter(lambda x: x != 0, map(lambda x: d[x], d)))
        self.result = 0

        while balances:
            q = []
            q.append((balances[0], [0], 1))
            balances = self.bfs(q, balances)

        return self.result

    def bfs(self, q, balances):
        n = len(balances)

        while q:
            total, path, start = q.pop(0)
            if not total: break
            for i in range(start, n):
                q.append((total + balances[i], path + [i], i + 1))

        self.result += len(path) - 1 # edges are payments and nodes are people
        path = set(path)
        return [balances[i] for i in range(n) if i not in path]

1  0

1   1
  2


# 465. Optimal Account Balancing
# https://leetcode.com/problems/optimal-account-balancing/description/

# Intutition
# 1. The graph is modelled as follows:
# 2. nodes are people and weighted edges are payments

# Approach 1: Backtracking
# 1. Use every transaction to build a ledger (dict) of balances for each person i, i is key and balance is value
# 2. Use the 

# Approach 2: BFS


# 1. First we need to count the net balance for every person, we define it as the list "balances[i]".
# 2. The question is the same as finding the "loop" in a graph (which the sum of elements in each graph is 0)
#    say, the answer is len(net) - number of circles.
# 3. Thus, in order to minimize the answer, we need to maximize the number of circles,
#    so we need to let every circle become "smaller", which is the same as "shortest path in a circle",
#    we can use BFS to solve it.
# 4. For BFS we do it in this way
#     - For every node, we look at all possible neighbours (i from start to n - 1)
#     - We do a boom boom boom node level by level until we reach a zero total path weight
#     - We break the while when total of the path weight reaches 0 and use the path constructed
#       or when q becomes empty
#     - The nodes in the path constructed are the unresolved debt for the BFS'ed cycle
#     - So we then start the next BFS from the 1st node of the path from the previous BFS
