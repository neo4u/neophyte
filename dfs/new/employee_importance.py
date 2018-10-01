# Algorithm

# Build a graph using employee data. Use a dictionary to represent it.
# Do a DFS on the graph.
class Solution:
    def score(self, id, graph, visited):
        visited.add(id)
        score = graph[id].importance
        for nbr in graph[id].subordinates:
            if nbr not in visited:
                score += self.score(nbr, graph, visited)
        return score
    
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        graph = {}
        for employee in employees:
            graph[employee.id] = employee
        visited = set([])
        return self.score(id, graph, visited)