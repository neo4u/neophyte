import sys
import collections

# Parse through entire snakes and ladders list
def build_graph(snakes, ladders):
    snakes_dict = {(s0 - 1): (s1 - 1) for s0, s1 in snakes}
    ladders_dict = {(l0 - 1): (l1 - 1) for l0, l1 in ladders}
    graph = [[] for _ in range(100)]

    # first we have 100 nodes indexed by 0 - 99
    for i in range(100):
        # For 1 - 6 we use the index to save an adacency list of connected nodes
        for dice_roll in range(1, 7):
            j = i + dice_roll       # We add the dice count to the current index which marks our curr node
            if j in snakes_dict:    # If j marks a snake start we calc our connected node use the snakes dict
                j = snakes_dict[j]
            elif j in ladders_dict: # If j marks a ladder bottom we calc our connected node use the ladder dict
                j = ladders_dict[j]

            if j <= 99:
                graph[i].append(j)  # We add an edge

    return graph


# Breadth-first search
def bfs(graph):
    queue = collections.deque([0])
    # We maintain a distance matrix to track the distance from 0, since BFS this is guaranteed to shortest distance
    distance = [0] + [-1] * 99

    # We start from 0
    while queue:
        i = queue.popleft()

        # For each neighbour
        for j in graph[i]:
            if distance[j] == -1:
                if j == 99: return distance[i] + 1  # If we reach 99 return the distance
                distance[j] = distance[i] + 1       # For each node that is not 99, we increment the distance
                queue.append(j)

    return -1


def quickest_way_up(snakes, ladders):
    """
    You are pass lists of tuples indicating source node
    and destination node for both snakes and ladders
    """
    graph = build_graph(snakes, ladders)
    return bfs(graph)


# Read input and start bfs
if __name__ == '__main__':
    f = sys.stdin
    T = int(f.readline().rstrip())

    for t in range(T):
        snakes, ladders = [], []
        num_snakes = int(f.readline().rstrip())

        for i in range(num_snakes):
            snakes.append(tuple(map(int, f.readline().rstrip().split())))
        num_ladders = int(f.readline().rstrip())

        for i in range(num_ladders):
            ladders.append(tuple(map(int, f.readline().rstrip().split())))
        print(quickest_way_up(snakes, ladders))

# Expected output
# 3
# 5

# Time: O(100)
# Space: O(100)