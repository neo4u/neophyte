class Solution(object):
	def leastInterval(self, tasks, n):
			"""
			:type tasks: List[str]
			:type n: int
			:rtype: int
			"""
			count = []
			tasks = sorted(tasks)
			index = 0

			while index < len(tasks):
				temp = tasks[index]
				c = 0

				while index < len(tasks) and temp == tasks[index]:
					c += 1
					index += 1

				count.append(c)

			count = sorted(count, reverse=True)
			r = 0

			while True:
				length = 1
				if len(count) - 1 < n:
						length = len(count)
				elif n >= 1:
						length = n + 1
				for i in range(length):
						count[i] -= 1
				count = sorted(count, reverse=True)
				r += length
				i = len(count) - 1
				while len(count) != 0 and count[i] == 0:
						del count[i]
						i -= 1
				if len(count) == 0:
						return r
				if length - 1 < n:
						r += n - length + 1