// People have posted elegant solutions using DP. 
// The solution I post below using BFS is no better than those.
// We can use a graph to represent the possible solutions.
// The vertices of the graph are simply the positions of the first characters of the words
// and each edge actually represents a word.
// For example, the input string is "nightmare", there are two ways to break it,
// "night mare" and "nightmare". The graph would be
// 0-->5-->9
// |__ __ _^
// The question is simply to check if there is a path from 0 to 9.
// The most efficient way is traversing the graph using BFS with the help of a queue and a hash set.
// The hash set is used to keep track of the visited nodes to avoid repeating the same work.
// For this problem, the time complexity is O(n^2) and space complexity is O(n), the same with DP.
// This idea can be used to solve the problem word break II.
// We can simple construct the graph using BFS, save it into a map and then find all the paths using DFS.

bool wordBreak(string s, unordered_set<string> &dict) {
    // BFS
    queue<int> BFS;
    unordered_set<int> visited;
    
    BFS.push(0);
    while(BFS.size() > 0)
    {
        int start = BFS.front();
        BFS.pop();
        if(visited.find(start) == visited.end())
        {
            visited.insert(start);
            for(int j=start; j<s.size(); j++)
            {
                string word(s, start, j-start+1);
                if(dict.find(word) != dict.end())
                {
                    BFS.push(j+1);
                    if(j+1 == s.size())
                        return true;
                }
            }
        }
    }
    
    return false;
}

/*
 SOLUTION 1: bfs
    Idea is to try to chop off prefix of s that is in the dict
    enqueue the left-over of each chop off
    if there is a time the left over happens to be in the dict as well
        we know word is breakable, b/c all the previous chops are all in the dict
    otherwise the original world is not breakable.
    
    we can use a set to store all the leftovers that we have tried, to avoid enqueue the 
    same leftover multiple times.

*/
public class Solution2 {
    public boolean wordBreak(String s, Set<String> wordDict) {
        int index = 0;
        Queue<String> queue = new LinkedList<String>();
        queue.offer(s);
        Set<String> visited = new HashSet<String>();

        while(!queue.isEmpty()){
            String candidate = queue.poll();
            if(wordDict.contains(candidate)) return true;

            for(int i = 0; i < candidate.length(); i++){
                String chop = candidate.substring(0,i);
                String next = candidate.substring(i, candidate.length());

                if(!visited.contains(next) && wordDict.contains(chop)){
                    next = candidate.substring(i, candidate.length());
                    queue.offer(next);
                    visited.add(next);
                }
            }
        }
        return false;
    }
}