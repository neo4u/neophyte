def findDuplicate(self, paths):
    M = collections.defaultdict(list)
    for line in paths:
        data = line.split()
        root = data[0]
        for file in data[1:]:
            name, _, content = file.partition('(')
            M[content[:-1]].append(root + '/' + name)
            
    return [x for x in M.values() if len(x) > 1]

# 609. Find Duplicate File in System
# https://leetcode.com/problems/find-duplicate-file-in-system/

# After parsing, we have some path and content.
# Let's store a map M[content] = [path1, path2, ...].
# At the end, we want all values in this map with length > 1.
