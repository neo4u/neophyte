# [(5, 15, 20), (10, 20, 30), (7, 25, 10)]


# 5 100, 5 6, 5 200
# a = 5
# b = 10
# c = 15
# d = 20

#     (10,15, 25)
#         /    \
# (5,10, 20)   (15,20, 30)

# [(5, 15, 20), (7, 25, 10), (10, 20, 30)]

# [5, 7, 20], [7, 10, (20 + 10)] [10, 15, [20 + 10]], [15, 20, 30], [20, 25 ,10], []
# 
# [5, 7, 20], 

# input = [(5, 15, 20), (10, 20, 30)]
# output = (5, 10, 20), (10, 15, (20 + 30)//2), (15, 20, 30)
# output = (5, 10, 20), (10, 15, 25), (15, 20, 30)

# input = [(5, 15, 20), (10, 20, 30), (7, 25, 10)]
# output = [(5, 10, 20), (10, 15, 25), (15, 20, 30)] merged with (7, 25, 10)
# output = [(5, 7, 20), (7, 10, (20 + 10)//2), (10, 15, (25 + 10)//2), (15, 20, (30 + 10)//2), (20, 25, 10)
# output = [(5, 7, 20), (7, 10, 15), (10, 15, 17.5), (15, 20, 20), (20, 25, 10)


class Node:
    def __init__(self, s, e, sp):
        self.s, self.e, self.sp = s, e, sp
        self.left, self.right = None, None

class Events:
    def __init__(self):
        self.root = None

    def insert(self, s, e, sp):
        if not self.root:
            root = Node(s, e, sp)
            return

        self._insert(s, e, sp, root)

    def _insert(self, s, e, sp, i_root):
        if s == e: return

        if e <= i_root.s:
            self._insert(s, e, sp, i_root.left)
        elif s >= i_root.e:
            self._insert(s, e, sp, i_root.right)
        else:
            a = min(i_root.s, s)
            b = max(i_root.s, s)
            c = min(i_root.e, e)
            d = max(i_root.e, e)

            if i_root.s != s and i_root.s == b:
                left_sp = sp
            else:
                left_sp = i_root.sp

            if i_root.e != e and i_root.e == c:
                right_sp = sp
            else:
                right_sp = i_root.sp

            self._insert(a, b, left_sp, i_root.left)
            self._insert(c, d, right_sp, i_root.right)
            i_root.sp = (i_root.sp + sp) / 2


# return in order traversal

# root: [10 20] 10
# new:  [0  30] 20

#      20 15 20
#     0 10 20 30


# root: [10 20] 10
# new:  [15 17] 20

#    10 15 10
#   10 15 17 20

# root: [10 20] 10
# new: [15 25] 20
# 10 15 20 25
#    (15, 20, 15)
#   /           \
# (10,15,10)    (20,25,20)



