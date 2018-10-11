// As suggested by the hints, this problem is equivalent to detecting a cycle in the graph represented by prerequisites. Both BFS and DFS can be used to solve it using the idea of topological sort. If you find yourself unfamiliar with these concepts, you may refer to their wikipedia pages.
// Specifically, you may only need to refer to the link in the third hint to solve this problem.
// Since pair<int, int> is inconvenient for the implementation of graph algorithms,
// we first transform it to a graph. If course u is a prerequisite of course v,
// we will add a directed edge from node u to node v.

// BFS
// BFS uses the indegrees of each node. We will first try to find a node with 0 indegree.
// If we fail to do so, there must be a cycle in the graph and we return false.
// Otherwise we have found one. We set its indegree to be -1 to prevent
// from visiting it again and reduce the indegrees of all its neighbors by 1.
// This process will be repeated for n (number of nodes) times.
// If we have not returned false, we will return true.

class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<unordered_set<int>> graph = make_graph(numCourses, prerequisites);
        vector<int> degrees = compute_indegree(graph);
        for (int i = 0; i < numCourses; i++) {
            int j = 0;
            for (; j < numCourses; j++)
                if (!degrees[j]) break;
            if (j == numCourses) return false;
            degrees[j] = -1;
            for (int neigh : graph[j])
                degrees[neigh]--;
        }
        return true;
    }
private:
    vector<unordered_set<int>> make_graph(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<unordered_set<int>> graph(numCourses);
        for (auto pre : prerequisites)
            graph[pre.second].insert(pre.first);
        return graph;
    }
    vector<int> compute_indegree(vector<unordered_set<int>>& graph) {
        vector<int> degrees(graph.size(), 0);
        for (auto neighbors : graph)
            for (int neigh : neighbors)
                degrees[neigh]++;
        return degrees;
    }
};

// https://www.youtube.com/watch?time_continue=1&v=ddTC4Zovtbc