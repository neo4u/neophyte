class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		queue = [(beginWord,1)]
		HashWord = {}
		while(len(queue) > 0 and 0 < len(wordList)):
			target, level = queue[0]
			if target == endWord:
					return HashWord[endWord]
			del queue[0]
			w = 0

		while(w < len(wordList)):
			if wordList[w] not in HashWord and self.isAdj(target, wordList[w]):
				HashWord[wordList[w]] = level + 1
				queue.append((wordList[w], level + 1))
				del wordList[w]
			else:
				w += 1
		if endWord in HashWord:
			return HashWord[endWord]
		else:
			return 0

	def isAdj(self, target, word):
		count = 0
		for i in range(len(word)):
			if target[i] != word[i]:
				count += 1
		if count == 1:
			return True
		else:
			return False