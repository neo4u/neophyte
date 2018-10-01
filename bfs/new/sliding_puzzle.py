import collections

class Solution:
    def slidingPuzzle(self, board):
        moves, used, cnt = {0: {1, 3}, 1:{0, 2, 4}, 2:{1, 5}, 3:{0, 4}, 4:{1, 3, 5}, 5:{2, 4}}, set(), 0
        s = "".join(str(c) for row in board for c in row)
        q = [(s, s.index("0"))]

        while q:
            new = []

            for s, i in q:
                used.add(s)
                if s == "123450":
                    return cnt
                arr = [c for c in s]

                for move in moves[i]:
                    new_arr = arr[:]
                    new_arr[i], new_arr[move] = new_arr[move], new_arr[i]
                    new_s = "".join(new_arr)

                    if new_s not in used:
                        new.append((new_s, move))

            cnt += 1
            q = new

        return -1

class Solution2(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        R, C = len(board), len(board[0])
        start_list = []
        for i in range(0, R):
            start_list += board[i]
        start = tuple(start_list)
        target = tuple(range(1, R*C) + [0])
        start_idx = start.index(0)
        queue = collections.deque([(start, start_idx, 0)])
        visited = {start}

        while queue:
            state, pos, depth = queue.popleft()
            if state == target:
                return depth
            for d in ((0,-1), (1,0), (0,1), (-1,0)):
                r, c = pos/C , pos%C
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < R and 0 <= nc < C:
                    npos = nr*C + nc
                    nstate = list(state)
                    nstate[pos], nstate[npos] = nstate[npos], nstate[pos]
                    nstate = tuple(nstate)
                    if nstate not in visited:
                        visited.add(nstate)
                        queue.append((nstate, npos, depth+1))

        return -1

# Well, this is my first try to post my solution.
# I would appreciate it if someone can make it cleaner.
class Solution3(object):
    def slidingPuzzle(self, board):
        state = "".join([str(n) for row in board for n in row])
        ans = "123450"
        if state ==ans:
            return 0

        mem = set()
        mem.add(state)
        # remember steps count in the queue
        queue = [(state,0)]

        # specify four swap conditions
        conditions = [
                (lambda x: x-1>=0 and x !=3, -1),
                (lambda x: x-3>=0 ,          -3),
                (lambda x: x+1< 6 and x !=2, 1),
                (lambda x: x+3< 6 ,          3)]

        while queue:
            state, step= queue.pop(0)
            zp = state.find('0')
            for c in conditions:
                if c[0](zp):
                    # swap
                    nstate= [s for s in state]
                    nstate[zp],nstate[zp+c[1]]=nstate[zp+c[1]],nstate[zp]
                    nstate= "".join(nstate)
                    
                    if nstate ==ans:
                        return step+1
                    if nstate not in mem:
                        mem.add(nstate)
                        queue.append((nstate,step+1))
        return -1