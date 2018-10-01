from collections import deque
class Solution(object):
    def getImportance(self, ems, id):
        
        dic={}
        for e in ems:
            dic[e.id]=e
        
        substack=deque()
        substack.append(id)
        res=0
        while substack:
            s=substack.popleft()
            if s not in dic:return 'error'
            res+=dic[s].importance
            for p in dic[s].subordinates:
                substack.append(p)
        return res