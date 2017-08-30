#!/bin/python3

def validate(cpy):
  for i in range(len(cpy)-1):
    if cpy[i] == cpy[i+1]:
      return False
  return True

length = input().strip()
s = input().strip()
st = list(set(s))
max_len = 0
for x in range(len(st)):
  # print("st[x] of x is: %s" % (st[x]))
  for y in range(x+1, len(st)):
    # print("st[y] of y is: %s" % (st[y]))
    cpy = [c for c in s if c==st[x] or c==st[y]]
    # print(cpy)
    if validate(cpy):
      max_len = max(max_len, len(cpy))
print(max_len)

# "beabeefeab"