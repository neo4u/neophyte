from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = " ".join(sentence) + " "
        start, n = 0, len(s)

        for _ in range(rows):
            start += cols

            while start >= 0 and s[start % n] != " ":
                start -= 1
            start += 1

        return start // n


# 418. Sentence Screen Fitting
# https://leetcode.com/problems/sentence-screen-fitting/description/


# Intuition:
# - Imagine an infinite sentence that are concatenated by words from the given sentence, 'infiStr'.
#   We want to cut the infiStr properly and put a piece at each row of the screen.
# - We maintain a pointer ptr. The ptr points to a position at infiStr, where next row will start. Cutting the 'infiStr'
#   and putting a piece at a row can be simulated as advancing the pointer by cols positions.
# - After advancing the pointer, if ptr points to a space, it means the piece can fit in row perfectly.
#   If ptr points to the middle of a word, we must retreat the pointer to the beginning of that word,
#   because a word cannot be split into two lines.
