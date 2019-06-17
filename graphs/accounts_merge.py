import collections

class DS:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def find(self, x):
        if x != self.parent[x]: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def has_parent(self, x):
        return x in self.parent

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False

        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1

        self.count -= 1
        return True

    def set_parent(self, x):
        self.parent[x] = x
        self.rank[x] = 0
        self.count += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_name_map, ds = {}, DS()
        for ac in accounts:
            name, *emails = ac
            for email in emails:
                email_name_map[email] = name
                if not ds.has_parent(email): ds.set_parent(email)
                ds.union(emails[0], email)

        ans = collections.defaultdict(list)
        for email in email_name_map:
            parent_email = ds.find(email)
            ans[parent_email].append(email)

        return [[email_name_map[emails[0]]] + sorted(emails) for emails in ans.values()]

# Accounts Merge