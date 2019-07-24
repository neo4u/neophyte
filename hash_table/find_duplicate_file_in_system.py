from typing import List
import collections
class Solution2:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_dict = collections.defaultdict(list)
        for path in paths:
            root, *files = path.split()
            for file in files:
                file_name, content = file[:-1].split('(')
                file_dict[content].append(root + '/' + file_name)

        return [v for k, v in file_dict.items() if len(v) > 1]


import hashlib
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_dict = collections.defaultdict(list)
        for path in paths:
            root, *files = path.split()
            for file in files:
                file_name, content = file[:-1].split('(')
                digest = hashlib.md5(content.encode('utf8')).hexdigest()
                file_dict[digest].append(root + '/' + file_name)

        return [v for k, v in file_dict.items() if len(v) > 1]


# 609. Find Duplicate File in System
# https://leetcode.com/problems/find-duplicate-file-in-system/

# After parsing, we have some path and content.
# Let's store a map M[content] = [path1, path2, ...].
# At the end, we want all values in this map with length > 1.

sol = Solution()
assert sol.findDuplicate([
    "root/a 1.txt(abcd) 2.txt(efgh)",
    "root/c 3.txt(abcd)",
    "root/c/d 4.txt(efgh)",
    "root 4.txt(efgh)"]
) == [['root/a/1.txt', 'root/c/3.txt'], ['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt']]