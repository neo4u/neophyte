string1=raw_input().strip()
string2=raw_input().strip()

n, m = len(string1), len(string2)
lcs = [[0] * (m + 1) for _ in xrange(n + 1)]

for i, a in enumerate(string1):
    for j, b in enumerate(string2):
        # print i, j, a, b
        if a == b:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

print lcs
print lcs[n - 1][m - 1]