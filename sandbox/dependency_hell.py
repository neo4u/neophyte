import bisect

from collections import deque

def find_required(n, deps, installs):
    visited = [False] * n
    required_installs = set(installs)

    q = deque(installs)
    while q:
        install = q.popleft()
        visited[install] = True
        for x in deps[install]:
            required_installs.add(x)
            if not visited[x]:
                q.append(x)
    return len(required_installs), required_installs


def top_sort(n, forest, no_dependencies, required_installs, dependencies):
    ans = []
    forest = [set(x) for x in forest]
    queue = [x for x in no_dependencies if x in required_installs]
    dependencies = [set(x) for x in dependencies]
    visited = [False] * n

    while queue:
        curr_install = queue.pop(0)
        for v in forest[curr_install]:
            dependencies[v].discard(curr_install)
        if not visited[curr_install]:
            visited[curr_install] = True
            ans.append(curr_install + 1)
        for x in forest[curr_install]:
            if not visited[x] and x in required_installs and not dependencies[x]:
                bisect.insort_left(queue, x)
    return ans


def make_forest(n, dependencies):
    forest = [[] for _ in range(n)]
    no_dependencies = []
    for i in range(n):
        if not dependencies[i]:
            no_dependencies.append(i)
        for d in dependencies[i]:
            forest[d].append(i)
    return sorted(no_dependencies), forest


def solve(n, dependencies, installs, required_installs):
    no_dependencies, forest = make_forest(n, dependencies)
    return " ".join(
        map(str, top_sort(n, forest, no_dependencies, required_installs, dependencies))
    )


def main():
    for _ in range(int(input())):
        n, m = [int(x) for x in input().split()]
        dependencies = []
        for i in range(n):
            dependencies.append(sorted(int(x) - 1 for x in input().split()[1:]))
        installs = [int(x) - 1 for x in input().split()]
        num_required, required_installs = find_required(n, dependencies, installs)
        print(num_required)

        assert len(installs) == m

        print(solve(n, dependencies, installs, required_installs))


if __name__ == "__main__":
    main()
