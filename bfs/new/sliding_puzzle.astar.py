# Its standard to use A* search to solve n-puzzle problem, 
# and using Manhattan distance will make the heuristic consistent, 
# in which case, we don't have to expand nodes that are already expanded and moved to the closed state.
from collections import heapq

class Solution:
    def slidingPuzzle(self, board):
        self.goal = [[1,2,3], [4,5,0]]
        self.score = [0] * 6

        self.score[0] = [[3, 2, 1], [2, 1, 0]]
        self.score[1] = [[0, 1, 2], [1, 2, 3]]
        self.score[2] = [[1, 0, 1], [2, 1, 2]]
        self.score[3] = [[2, 1, 0], [3, 2, 1]]
        self.score[4] = [[1, 2, 3], [0, 1, 2]]
        self.score[5] = [[2, 1, 2], [1, 0, 1]]

        heap = [(0, 0, board)]
        closed = []

        while len(heap) > 0:
            node = heapq.heappop(heap)
            if node[2] == self.goal:
                return node[1]
            elif node[2] in closed:
                continue
            else:
                for next in self.get_neighbors(node[2]):
                    if next in closed: continue
                    heapq.heappush(heap, (node[1] + 1 + self.get_score(next), node[1] + 1, next))
            closed.append(node[2])
        return -1

    def get_neighbors(self, board):
        res = []
        if 0 in board[0]:
            r, c = 0, board[0].index(0)
        else:
            r, c = 1, board[1].index(0)

        for offr, offc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= r + offr < 2 and 0 <= c + offc < 3:
                board1 = copy.deepcopy(board)
                board1[r][c], board1[r+offr][c+offc] = board1[r+offr][c+offc], board1[r][c]
                res.append(board1)
        return res


    def get_score(self, board):
        score = 0
        for i in range(2):
            for j in range(3):
                score += self.score[board[i][j]][i][j]
        return score

# Found some time to shorten some of the methods after the contest, here is the revised version:
class Solution2:
    def slidingPuzzle(self, board):
        self.scores = [0] * 6
        goal_pos = {1:(0, 0), 2:(0, 1), 3: (0, 2), 4: (1,0), 5:(1,1), 0:(1, 2)}

        for num in range(6): # Pre calculate manhattan distances
            self.scores[num] = [[abs(goal_pos[num][0] - i) + abs(goal_pos[num][1] - j) for j in range(3)] for i in range(2)]

        Node = namedtuple('Node', ['heuristic_score', 'distance', 'board'])
        heap = [Node(0, 0, board)]
        closed = []

        while len(heap) > 0:
            node = heapq.heappop(heap)
            if self.get_score(node.board) == 0:
                return node.distance
            elif node.board in closed:
                continue
            else:
                for neighbor in self.get_neighbors(node.board):
                    if neighbor in closed: continue
                    heapq.heappush(heap, Node(node.distance + 1 + self.get_score(neighbor), node.distance + 1, neighbor))
            closed.append(node.board)
        return -1

    def get_neighbors(self, board):
        r, c = (0, board[0].index(0)) if 0 in board[0] else (1, board[1].index(0))
        res = []

        for offr, offc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= r + offr < 2 and 0 <= c + offc < 3:
                board1 = copy.deepcopy(board)
                board1[r][c], board1[r+offr][c+offc] = board1[r+offr][c+offc], board1[r][c]
                res.append(board1)
        return res

    def get_score(self, board):
        return sum([self.scores[board[i][j]][i][j] for i in range(2) for j in range(3)])
