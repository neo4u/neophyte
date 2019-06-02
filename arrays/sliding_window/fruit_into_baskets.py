class Solution:
    def totalFruit(self, tree):
        l, r = 0, 0
        fruit_map, max_len = {}, 0

        while r < len(tree):
            fruit_map[tree[r]] = fruit_map.get(tree[r], 0) + 1

            while len(fruit_map) > 2:
                fruit_map[tree[l]] -= 1
                if not fruit_map[tree[l]]:
                    del fruit_map[tree[l]]
                l += 1

            max_len = max(r - l + 1, max_len)
            r += 1

        return max_len