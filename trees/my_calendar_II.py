class MyCalendarTwo:
	
	def __init__(self):
		self.root = None

	def book(self, start, end):
		"""
		:type start: int
		:type end: int
		:rtype: bool
		"""
		if not self.is_insertable(start, end, self.root):
			return False

		self.root = self.insert(start, end, self.root)
		return True

	def is_insertable(self, start, end, root):
		if not root:
			return True

		if start >= end:
			return True

		if end <= root.start:
			return self.is_insertable(start, end, root.left)

		elif start >= root.end:
			return self.is_insertable(start, end, root.right)

		else: #overlap
			if root.single_overlap:
				return False
			elif start >= root.start and end <= root.end:
				return True
			else:
				return self.is_insertable(start, root.start, root.left) and self.is_insertable(root.end, end, root.right)

	def insert(self, start, end, root):
		if not root:
			root = Node(start, end)
			return root

		if start >= end:
			return root

		if start >= root.end:
			root.right = self.insert(start, end, root.right)

		elif end <= root.start:
			root.left = self.insert(start, end, root.left)

		else:
			root.single_overlap = True
			a = min(root.start, start)
			b = max(root.start, start)
			c = min(root.end, end)
			d = max(root.end, end)
			root.start, root.end = b, c
			root.left, root.right = self.insert(a, b, root.left), self.insert(c, d, root.right)

		return root

class Node:
	"""
	:type left: Node
	:type right: Node
	:type single_overlap: bool
	"""
	def __init__(self, start, end):
		"""
		:type start: int
		:type end: int
		"""
		self.start = start
		self.end = end
		self.left = None
		self.right = None
		self.single_overlap = False

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
