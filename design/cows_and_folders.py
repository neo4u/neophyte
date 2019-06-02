# Problem Description: In a folder system there are:
# -shared folders
# -confidential folders

# Each folder has a list of cows that are explicit members of the folder.
# If you are an explicit member, you can access that folder
# and all its non-confidential child folders through inheritance A folder is called a leaf
# if it is not the parent of any other folder.

# A cow is uncool if there is at least one leaf they cannot access.
# Determine which cows are uncool. Input: 3
# Q cows 2 
# M shared folders,
# N confidential folders 1 1 0
# folder id of shared, K cows have explicit access, K ids (M=2) 2 1 1
# folder id of shared, K cows have explicit access, K ids (M=2) 3 3 0 1 2
# folder id of confidential, K cows with explicit access, K ids 2
# single non-negative int G    1 2 U,V.
# U folder id of parent, V child folder id (G=2) 1 3
# U,V. U folder id of parent, V child folder id (G=2) Output:
# (Return ID of uncool cow, cow that cannot access at least one leaf)
# 2 SF1 / \ SF2 CF3 SF1 (0) / \ SF2 (0,1) CF3 (0,1,2)
# Cow 0 has access to SF1 id=1 (1 1 0)
# Cow 1 has access to SF2 id=2 (2 1 1)
# Cow 0 also has access because folder id=1 is a parent of folder id=2 (1 2)
# Cow 0,1,2 has access to CF3 id=3 (3 3 0 1 2)
# Cow 2 cannot access SF2 id=2, so return 2.
# Custom input: (Becomes tree below)
# 4 4 2 1 2 0 2 2 1 3 5 1 1 6 3 0 1 3 3 0 4 3 0 1 2 5 1 2 1 3 2 4 2 5 3 6
# (Unshaded nodes = shared folders, shaded nodes = confidential nodes in the picture)
# Expected output: 2,3 (the cows that don't have access to all leaf nodes)


# import sys

# data = sys.stdin.read().splitlines()
data = ['4', '4 2', '1 2 0 2 ', '2 1 3 ', '5 1 1', '6 3 0 1 3', '3 0 ', '4 3 0 1 2', '5', '1 2', '1 3', '2 4', '2 5', '3 6']
sdata = []

for row in data:
    sdata.append(row.split())

#print(sdata)

Q = int(sdata[0][0]) #num cows
M = int(sdata[1][0]) #num shared folders
N = int(sdata[1][1]) #num confidential folders
G = int(sdata[2+M+N][0]) #num folder edges
#print(Q, M, N, G)

nodenames = []
shared = []
confidential = []
for i in range(0, M):
    n_name = sdata[1+1+i][0]
    nodenames.append(n_name)
    shared.append(n_name)
for i in range(0, N):
    n_name = sdata[1+1+M+i][0]
    nodenames.append(n_name)
    confidential.append(n_name)
# print(nodenames)
# print(shared)
# print(confidential)


nodelist = {} #map of node: children
for node in nodenames:
    nodelist[node] = []
#print(nodelist)

for i in range(0, G): #loop for G # of edges
    parent = sdata[3+M+N+i][0]
    child = sdata[3+M+N+i][1]
    
    if parent not in nodelist:
        nodelist[parent] = [child]
    else:
        nodelist[parent].append(child)
#print(nodelist)


accesslist = {} #map of node: cows that have access
for i in range(1+1, 1+1+M+N):
    node = sdata[i][0]
    numcows = int(sdata[i][1])
    accesslist[node] = []
    for j in range(0, numcows):
        accesslist[node].append(sdata[i][1+1+j])
#print(accesslist)


#update recursively which nodes can be accessed by which cow
def grantPermissions(nodelist, accesslist, sharedlist):
    for node in accesslist:
        for child in nodelist[node]:
            if child in sharedlist:
                for cow in accesslist[node]:
                    if cow not in accesslist[child]:
                        accesslist[child].append(cow)
                        grantPermissions(nodelist, accesslist, sharedlist)


grantPermissions(nodelist, accesslist, shared)
#print(accesslist)

leaflist = []
for node in nodelist:
    if nodelist[node] == []:
        leaflist.append(node)
#print(leaflist)

cows = set(range(0,Q))
coolcows = set(range(0,Q))
#print(coolcows)
for leaf in leaflist:
    lst = accesslist[leaf]
    s = set(list(map(int, lst)))
    coolcows = coolcows.intersection(s)

#print(coolcows)
uncoolcows = cows.symmetric_difference(coolcows)
for sadcow in uncoolcows:
    print (sadcow)