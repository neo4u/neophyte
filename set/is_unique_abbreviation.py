#
# i18n - internationalization
# l10n - localization
#
# 1) Have you seen the abbreviations l10n, i18n ? Do you know what they stand for and how the abbreviation works?
# 2) Given a word and a list of words, implement a function to find abbreviation collisions.
#
# is_unique("hat", ["test", "hit", "blub"]) -> False
# is_unique("hat", ["test", "hid", "blub"]) -> True
# is_unique("hat", ["had", "hid", "blub"]) -> True
from typing import List


def is_unique(word: str, wlist: List[str]):
    abbr_set = set()

    for w in wlist:
        abbr = find_abbr(w)
        abbr_set.add(abbr)

    w_abbr = find_abbr(word)
    return w_abbr not in abbr_set

def find_abbr(word: str) -> int:
    n = len(word)
    if n <= 2: return word
    return word[0] + str(n - 2) + word[-1]

assert is_unique("hat", ["test", "hit", "blub"]) == False
assert is_unique("hat", ["test", "hit", "blub"]) == False

# isinstance(var, str)
# type() == str or int

# Time: O(n)
# Space: O(n)
