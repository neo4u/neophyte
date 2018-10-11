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

class Solution2(object):
   def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        emps = {employee.id: employee for employee in employees}
        print(emps)

        def dfs(id):
            sum = emps[id].importance
            for sub_id in emps[id].subordinates:
                sum += dfs(sub_id)
            return sum

        return dfs(id)


# Time Complexity: O(N), where NN is the number of employees. We might query each employee in dfs.
# Space Complexity: O(N), the size of the implicit call stack when evaluating dfs.