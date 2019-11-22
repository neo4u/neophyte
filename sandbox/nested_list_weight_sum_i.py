class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.dfs(nestedList, 1)

    def dfs(self, n_list, depth):
        n_sum = 0

        for item in n_list:
            if item.isInteger():
                n_sum += item.getInteger() * depth
            else:
                n_sum += self.dfs(item.getList(), depth + 1)

        return n_sum
