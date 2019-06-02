import random
class Solution:
    def kClosest(self, points, k):
        self.quick_select(points, k, 0, len(points) - 1)
        return points[:k]

    def distance(self, point):
        x, y = point[0], point[1]
        return x ** 2 + y ** 2

    def quick_select(self, points, k, l, r):
        q = self.rand_partition(points, k, l, r)
        if l >= r: return
        if q == k: return

        if k < q:
            self.quick_select(points, k, l, q - 1)
        else:
            self.quick_select(points, k, q + 1, r)

    def rand_partition(self, points, k, l, r):
        q = random.randint(l, r)
        points[r], points[q] = points[q], points[r]
        return self.partition(points, k, l, r)

    def partition(self, points, k, l, r):
        pivot = self.distance(points[r])
        i = l - 1

        for j in range(l, r):
            if self.distance(points[j]) >= pivot:
                continue
            i += 1
            points[j], points[i] = points[i], points[j]

        i += 1
        points[r], points[i] = points[i], points[r]
        return i


sol = Solution()
assert sol.kClosest([[0, 1], [1, 0]], 2) == [[0, 1], [1, 0]]
