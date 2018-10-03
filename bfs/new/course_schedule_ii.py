import collections

# BFS
def findOrder1(self, numCourses, prerequisites):
    dic = {i: set() for i in range(numCourses)}
    neigh = collections.defaultdict(set)

    for i, j in prerequisites:
        dic[i].add(j)
        neigh[j].add(i)

    # queue stores the courses which have no prerequisites
    queue = collections.deque([i for i in dic if not dic[i]])
    count, res = 0, []

    while queue:
        node = queue.popleft()
        res.append(node)
        count += 1
        for i in neigh[node]:
            dic[i].remove(node)
            if not dic[i]:
                queue.append(i)

    return res if count == numCourses else []
