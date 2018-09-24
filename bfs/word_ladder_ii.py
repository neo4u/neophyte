from collections import defaultdict, deque
import string
import json

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        explored = set()

        word_path = defaultdict(list)
        word_path[beginWord] = [[beginWord]]

        wordQue = deque([beginWord])

        while wordQue:
            print("word_path is")
            print(json.dumps(word_path, indent=2))
            word = wordQue.popleft()
            explored.add(word)

            for idx in range(len(word)):
                for new_c in string.ascii_lowercase:
                    if new_c != word[idx]:
                        new_word = word[:idx] + new_c + word[idx+1:]

                        if new_word in wordSet and new_word not in explored:
                            if new_word not in wordQue: # important
                                wordQue.append(new_word)

                            print("Word is: %s" % word)
                            print("new_word is: %s" % new_word)

                            for path in map(lambda path_parent: path_parent + [new_word], word_path[word]):
                                print("path is")
                                print(path)
                                print("word_path[new_word] is")
                                print(word_path[new_word])
                                if not word_path[new_word] or len(word_path[new_word][-1]) == len(path):
                                    print("pushing path")
                                    print(path)
                                    word_path[new_word].append(path)
                                    print("word_path is")
                                    print(json.dumps(word_path, indent=2))
                                else:
                                    break
                print("\n")
        return word_path[endWord]


solution = Solution()

print(solution.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
