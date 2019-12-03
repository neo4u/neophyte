from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i, n, result = 0, len(words), []

        while i < n:
            curr_line, j, line_len = [words[i]], i + 1, len(words[i])   # decide how many words to be put in one line
            pos, spaces = 0, maxWidth - len(words[i])

            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                curr_line.append(words[j])
                line_len += 1 + len(words[j])
                spaces -= len(words[j])
                pos += 1; j += 1
            i = j

            # decide the layout of one line
            if i < n and pos: spaces = [' ' * (spaces // pos + (k < spaces % pos)) for k in range(pos)] + ['']
            else:             spaces = [' '] * pos + [' ' * (maxWidth - line_len)]  # last line or the line only has one word

            result.append(''.join([s for pair in zip(curr_line, spaces) for s in pair]))

        return result

# Some variable meanings:
# 1. pos:       This is for index of the word within the line,
#               it also gives the number of space strings to contruct between words,
#               cuz, n words means n - 1 spaces in between
# 2. i:         variable to index into words
# 3. j:         j is our running index which we use to go from i + 1 and keep including words in curr line
# 4. spaces:    Number of spaces chars, that need to be distributed over 'pos' places
# 5. curr_line: List of words in the curr line
# 6. line_len:  This is len of the curr line if it were constructed simply as words interspersed with 1 space
# 7. spaces = [' ' * (spaces // pos + (k < spaces % pos)) for k in range(pos)] + ['']
#    This weird representation constructs the corresponding whitespace strings to be added to words in curr_line
#    Example:
#    spaces = 10 and pos = 4, leads to ['   ', '   ', '  ', '  ', ''] == [3, 3, 2, 2] + [0] spaces
#    this is because when we do 10 % 4 == 2, remainder from div by 4, which leaves two spaces to be distributed,
#    which we place in the first two indexes in range(pos) or range(4), i.e. so 0, 1 get 3 spaces and 2, 3 get 2 spaces
#    which gives us the idea that if k < spaces % pos, we given it 1 more space, and hence we get:
#    ' ' * (spaces // pos + (k < spaces % pos)) for range(pos)] + [''],
#    The + [''] at the end is to add to the word pos+1th word, everything before is to concat to earlier words,
#    last words concats with ''
#    spaces = 10 and pos = 5, leads to ['  ', '  ', '  ', '  ', '  ', ''] == [2, 2, 2, 2] + [0] spaces


# 68. Text Justification
# https://leetcode.com/problems/text-justification/description/


# Intuition:
# 1. One thing that is obvious is that we'll try to fit in
#    as many words as possible in sequence into the madWidth length
# 2. So as soon as we find a word doesn't fit in the curr line,
#    we distribute the spaces between words on the curr line
# 3. The key part is the distribution of spaces between words,
#    how is this going to be done in even cases and uneven cases?
# 4. We use the bool (k < spaces % pos) for k in range(pos) to either add a space or not for each space position


sol = Solution()
assert sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) == [
    "This    is    an",
    "example  of text",
    "justification.  "
]

assert sol.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16) == [
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
]
