
def remove_duplicates_from_string(s):
    bitset = 0
    i, n, final_len = 0, len(s), 0

    while i < n:
        c, bit_idx = s[i], ord(s[i]) - ord('a')
        if bitset & (1 << bit_idx) == 0:
            s = s[:final_len] + c + s[final_len + 1:]
            bitset |= 1 << bit_idx
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



# pairs=[(1,4),(6,8),(2,4),(7,9),(10,15)]
# hours = set()
# for first,last in pairs:
# 	i = first
# 	while i<=last:	
# 		print(i)
# 		hours.add(i)
# 		i+=1
# print("total hours=",len(hours))