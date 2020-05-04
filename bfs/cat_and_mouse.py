from typing import List


# class Solution:
#     def catMouseGame(self, graph: List[List[int]]) -> int:
        




# The explanation and original java code can be found here.
# https://leetcode.com/problems/cat-and-mouse/discuss/298937/DP-memory-status-search-search-strait-forward-and-easy-to-understand

# Modify the code based on @aaardvark commet to make it more concise.

from functools import lru_cache
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        return self.search(graph, 0, 1, 2)

    @lru_cache(None)
    def search(self, graph, t, x, y):
        if t == len(graph) * 2: return 0
        if x == y: return 2
        if x == 0: return 1
        if t % 2 == 0: # mouse's turn. Mouse will win if the mouse can find any winable node for the next step. If all the next step is winable for cats, then mouse lose.
            if any(self.search(graph, t + 1, x_nxt, y) == 1 for x_nxt in graph[x]): return 1
            if all(self.search(graph, t + 1, x_nxt, y) == 2 for x_nxt in graph[x]): return 2
            return 0
        else:# cat's turn
            if any(self.search(graph, t + 1, x, y_nxt) == 2 for y_nxt in graph[y] if y_nxt != 0): return 2
            if all(self.search(graph, t + 1, x, y_nxt) == 1 for y_nxt in graph[y] if y_nxt != 0): return 1
            return 0


import collections
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        DRAW, MOUSE, CAT = 0, 1, 2

        for node, neighbors in enumerate(graph):
            graph[node] = set(neighbors)

        def neighborhood(player, cat, mouse):
            if player == CAT:
                for next_mouse in graph[mouse]:
                    yield MOUSE, cat, next_mouse
            else:
                for next_cat in graph[cat]:
                    if next_cat:
                        yield CAT, next_cat, mouse

        q = collections.deque()
        state = collections.defaultdict(lambda: DRAW)
        draws_left = {}

        for cat in range(n):
            for mouse in range(n):
                draws_left[MOUSE, cat, mouse] = len(graph[mouse])
                draws_left[CAT, cat, mouse] = len(graph[cat]) - (0 in graph[cat])

        for cat in range(n):
            state[MOUSE, cat, 0] = state[CAT, cat, 0] = MOUSE
            q.extend([(MOUSE, cat, 0, MOUSE), (CAT, cat, 0, MOUSE)])

        for pos in range(1, n):
            state[MOUSE, pos, pos] = state[CAT, pos, pos] = CAT
            q.extend([(MOUSE, pos, pos, CAT), (CAT, pos, pos, CAT)])

        while q:
            player, cat, mouse, winner = q.popleft()

            for player2, cat2, mouse2 in neighborhood(player, cat, mouse):
                if state[player2, cat2, mouse2] == DRAW:
                    draws_left[player2, cat2, mouse2] -= 1

                    if player2 == winner or not draws_left[player2, cat2, mouse2]:
                        if player2 == MOUSE and cat2 == CAT and mouse2 == MOUSE:
                            return winner

                        state[player2, cat2, mouse2] = winner
                        q.append((player2, cat2, mouse2, winner))

        return state[MOUSE, CAT, MOUSE]


class Solution:
    '''
    The idea of Topological traversal is start from each ending status,
    topologically traversal to color the previous status.
    '''
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        # (cat, mouse, mouseMove = 0)
        color = [[[0]*2 for _ in range(n)] for _ in range(n)]
        #out degree for each node, 0 from i->j, 1 from j->i and cat
        outdegree = [[[0]*2 for _ in range(n)] for _ in range(n)]
        for i in range(n): # cat
            for j in range(n): # mouse
                outdegree[i][j][0] = len(graph[j]) # for mouse
                outdegree[i][j][1] = len(graph[i]) # for cat
                for k in graph[i]:
                    if not k:
                        outdegree[i][j][1] -= 1
                        break

        # cat,mouse,mouseMove,result
        # return 1 if the game is won by Mouse, 2 if the game is won by Cat, and 0 if the game is a draw.
        q = collections.deque()
        for k in range(1, n):
            for m in range(2):
                # start from each ending status
                color[k][0][m] = 1 # mouse at hole, mouse win, result is 1
                q.append((k, 0, m, 1))
                color[k][k][m] = 2 # cat and mouse at the same position, cat win, result is 2
                q.append((k, k, m, 2))

        while q:
            cat, mouse, mouseMove, result = q.popleft()
            # mouseMove is 0 means mouse finished move, cat should move ; 1 - cat finished move
            if cat == 2 and mouse == 1 and mouseMove == 0: return result
            prevMouseMove = 1 - mouseMove

            for prev in graph[cat if prevMouseMove == 1 else mouse]:
                # if should cat move, cat back, otherwise stand still
                prevCat = prev if prevMouseMove == 1 else cat
                prevMouse = mouse if prevMouseMove == 1 else prev

                if prevCat == 0: continue                               # cat cannot go to hole
                if color[prevCat][prevMouse][prevMouseMove]: continue   # already done

                if prevMouseMove == 1 and result == 2 or prevMouseMove == 0 and result == 1:
                    # new ending status
                    color[prevCat][prevMouse][prevMouseMove] = result
                    q.append((prevCat, prevMouse, prevMouseMove, result))
                else:
                    outdegree[prevCat][prevMouse][prevMouseMove] -= 1
                    if not outdegree[prevCat][prevMouse][prevMouseMove]:
                        color[prevCat][prevMouse][prevMouseMove] = result
                        q.append((prevCat, prevMouse, prevMouseMove, result))

        return color[2][1][0]



class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)

        # What nodes could play their turn to
        # arrive at node (m, c, t) ?
        def parents(m, c, t):
            if t == 2:
                for m2 in graph[m]:
                    yield m2, c, 3-t
            else:
                for c2 in graph[c]:
                    if c2:
                        yield m, c2, 3-t

        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int)

        # degree[node] : the number of neutral children of this node
        degree = {}
        for m in range(N):
            for c in range(N):
                degree[m,c,1] = len(graph[m])
                degree[m,c,2] = len(graph[c]) - (0 in graph[c])

        # enqueued : all nodes that are colored
        queue = collections.deque([])
        for i in range(N):
            for t in range(1, 3):
                color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))

        # percolate
        while queue:
            # for nodes that are colored :
            i, j, t, c = queue.popleft()
            # for every parent of this node i, j, t :
            for i2, j2, t2 in parents(i, j, t):
                # if this parent is not colored :
                if color[i2, j2, t2] is DRAW:
                    # if the parent can make a winning move (ie. mouse to MOUSE), do so
                    if t2 == c: # winning move
                        color[i2, j2, t2] = c
                        queue.append((i2, j2, t2, c))
                    # else, this parent has degree[parent]--, and enqueue if all children
                    # of this parent are colored as losing moves
                    else:
                        degree[i2, j2, t2] -= 1
                        if degree[i2, j2, t2] == 0:
                            color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3 - t2))

        return color[1, 2, 1]


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        def parents(m, c, t):
            if t == CAT_TURN:
                for m2 in graph[m]:
                    yield m2, c, MOUSE_TURN
            else:
                for c2 in graph[c]:
                    if c2 != 0:
                        yield m, c2, CAT_TURN
        DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2
        MOUSE_TURN, CAT_TURN = 1, 2
        N = len(graph)
        degree = {}
        for m in range(N):
            for c in range(N):
                degree[m, c, MOUSE_TURN] = len(graph[m])
                degree[m, c, CAT_TURN] = len(graph[c]) - (0 in graph[c])
        color = collections.defaultdict(lambda: DRAW)
        q = collections.deque()
        for i in range(N):
            for turn in (MOUSE_TURN, CAT_TURN):
                color[0, i, turn] = MOUSE_WIN
                q.append((0, i, turn, MOUSE_WIN))
                if i > 0:
                    color[i, i, turn] = CAT_WIN
                    q.append((i, i, turn, CAT_WIN))
        while q:
            m1, c1, t1, w1 = q.popleft()
            for m2, c2, t2 in parents(m1, c1, t1):
                if color[m2, c2, t2] == DRAW:
                    if t2 == w1:
                        color[m2, c2, t2] = w1
                        q.append((m2, c2, t2, w1))
                    else:
                        degree[m2, c2, t2] -= 1
                        if degree[m2, c2, t2] == 0:
                            color[m2, c2, t2] = w1
                            q.append((m2, c2, t2, w1))
        return color[1, 2, MOUSE_TURN]


# 913. Cat and Mouse
# https://leetcode.com/problems/cat-and-mouse/description/
