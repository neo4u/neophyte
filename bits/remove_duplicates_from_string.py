def remove_duplicates_from_string(s):
    bitset = 0
    i, n, final_len = 0, len(s), 0

    while i < n:
        c, bit_idx = s[i], ord(s[i]) - ord('a')          # offset from 97
        if bitset & (1 << bit_idx) == 0:                 # check if xth bit of the counter
            s = s[:final_len] + c + s[final_len + 1:]
            bitset |= 1 << bit_idx                       # Set the xth bit of the counter
            final_len += 1
        i += 1

    return s[:final_len]


# Problem:
# Remove all duplicate characters from string.

# Time: O(n)
# Space: O(1)

# Works only if string has less than 32/64 characters a-z or whatever.

assert remove_duplicates_from_string('geeksforgeeks') == 'geksfor'
assert remove_duplicates_from_string('aaaabbbbbbccccccccccccdddddd') == 'abcd'
