TAB = '\t'

class Solution:
    def print_indent(self, s: str) -> None:
        self.dfs(0, s, 0)

    def dfs(self, i, s, depth):
        if i >= len(s) - 1: return len(s)

        curr = ''
        while i < len(s):
            c = s[i]
            if c == '(':
                if curr:
                    print(f"{TAB * depth}{curr}")
                    curr = ''
                print(f"{TAB * depth}(")
                i = self.dfs(i + 1, s, depth + 1)
                print(f"{TAB * depth})")
            elif c == ')':
                if curr:
                    print(f"{TAB * depth}{curr}")
                    curr = ''
                return i + 1    # skip the paren char
            elif c.isalpha() or c.isdigit():
                curr += c       # form the word
                i += 1
            elif c.isspace():
                print(f"{TAB * depth}{curr}")
                curr = ''
                i += 1


sol = Solution()
sol.print_indent("(hello word (bye bye))")
sol.print_indent("(hello word (bye(123)bye))")
sol.print_indent("(hello world (bye(123 456 789)world))")
