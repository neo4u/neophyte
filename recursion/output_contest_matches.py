class Solution(object):
    def findContestMatch(self, n):
        teams = [i for i in range(1, n + 1)]
        return self.generate_contest(teams)

    def generate_contest(self, teams):
        n = len(teams)
        if n == 1: return teams[0]

        level_teams = []
        for i in range(n // 2):
            item = f"({teams[i]},{teams[n - 1 - i]})"
            level_teams.append(item)

        return self.generate_contest(level_teams)


class Solution2(object):
    def findContestMatch(self, n):
        items = [i for i in range(1, n + 1)]

        while n > 1:
            for i in range(n // 2):
                items[i] = f"({items[i]},{items.pop()})"
            n /= 2
        return items[0]


class Solution3:
    def findContestMatch(self, n):
        res = list(map(str, range(1, n + 1)))
        while n > 1:
            res = ["(" + res[i] + "," + res[n - 1 - i] + ")" for i in range(n // 2)]
            n >>= 1
        return res[0]

# 10 = 0000 1010
# ‭-10= 1111 0110‬

#  0000 0010


# 1111 0101
#         1
# 1111 0110

# [1,2,3,4,5,6,7,8]
# [1,8  2,7    3,6   4,5]
# [1,8,4,5  2,7,3,6]
# [1,8,4,5,2,7,3,6]