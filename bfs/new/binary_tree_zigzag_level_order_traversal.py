# We can solve this problem by using BFS with queue. Level information is needed in order to reverse the odd row.

def zigzagLevelOrder(self, root):
    res, queue = [], [(root, 0)]
    while queue:
        curr, level = queue.pop(0)
        if curr:
            if len(res) < level+1:
                res.append([])
            if level % 2 == 0:
                res[level].append(curr.val)
            else:
                res[level].insert(0, curr.val)
            queue.append((curr.left, level+1))
            queue.append((curr.right, level+1))
    return res