''' implement cd

|  curr_dir   |          path             | output       |
| ----------- | ------------------------- | ------------ |
|  /          | ./a/b/c                   | /home/a/b/c  |
|  /home      | ./a/../b/c                | /home/b/c    |
|  /home      | ./a/../../b/c             | /home/c      |
|  /home      | ./a/../b/../c/../         | /home        |
|  /home      | ../../a/b/c               | /home/c      |
|  /home      | ../a/..//b/c              | /home/c      |

Pay attention to:
- What data structure is right?
- What is the complexity?
- What are the corner cases
'''

class Solution:
    def cd(self, curr_dir: str, path: str) -> str:



sol = Solution()
assert sol.cd('/' , './a/b/c') == '/home/a/b/c'
assert sol.cd('/home', './a/../b/c') == '/home/b/c'
assert sol.cd('/home', './a/../../b/c') == '/home/c'
assert sol.cd('/home', './a/../b/../c/../') == '/home'
assert sol.cd('/home', '../../a/b/c') == '/home/c'
assert sol.cd('/home', '../a/..//b/c') == '/home/c'
