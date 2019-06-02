class Solution:
    def expressiveWords(self, S, words):
        i, j = 0, 0
        s = []
        while j < len(S):
            while j < len(S)-1 and S[j] == S[j+1]:
                j += 1
            if j - i >= 2:
                s.append(S[j] + "{1," + str(j-i+1) + "}")
            else:
                s.append(S[j] * (j-i+1))
            j += 1
            i = j

        s = ''.join(s) + '$'
        ans = 0
        for word in words:
            if re.match(s, word):
                ans += 1
        return ans


class Solution:
    def expressiveWords(self, S, words):
        s_groups = self.capture_groups(S)
        result = 0

        for word in words:
            if len(word) > len(S): continue
            print(f'Processing word {word}')
            w_groups = self.capture_groups(word)
            if len(s_groups) != len(w_groups): continue

            i, j, found = 0, 0, True
            while i < len(word) and j < len(S):
                w_g = w_groups[i]
                s_g = s_groups[j]
                print(f'Processing group {w_g}')
                if w_g[0] != s_g[0] or (s_g[1] != w_g[1] and (w_g[1] > s_g[1] or s_g[1] < 3)):
                    found = False
                    print(f"Breaking cuz of mismatched groups w_g: {w_g}, s_g: {s_g}")
                    break

                i += w_g[1]
                j += s_g[1]
            if found:
                result += 1
                print(result)

            print('\n')

        print(result)
        return result

    def capture_groups(self, s):
        groups = {}
        i = 0

        while i < len(s):
            first_occurence = i
            while i < len(s) - 1 and s[i] == s[i + 1]: i += 1
            groups[first_occurence] = (s[first_occurence], i - first_occurence + 1)
            i += 1

        return groups

sol = Solution()
S, words = "heeellooo", ['helo', "hello", "hi"]
assert sol.expressiveWords(S, words) == 1

print(sol.capture_groups("dddiiiinnssssssoooo"))
S = "dddiiiinnssssssoooo"
words = ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]
assert sol.expressiveWords(S, words) == 3

# 809. Expressive Words
# https://leetcode.com/problems/expressive-words/description/

# {0: ('h', 1), 1: ('e', 3), 4: ('l', 2), 6: ('o', 3)}
# {0: ('h', 1), 1: ('e', 1), 2: ('l', 2), 4: ('o', 1)}
# {0: ('h', 1), 1: ('i', 1)}
# {0: ('h', 1), 1: ('e', 1), 2: ('l', 1), 3: ('o', 1)}
