import java.util.*;

public class Solution {
    public char recommend(char tar, char[][] arr) {
        HashMap<Character, HashSet<Character>> graph = new HashMap<Character, HashSet<Character>>();
        HashMap<Character, Integer> SndIndegree = new HashMap<Character, Integer>();

        //build graph
        for (char[] edge : arr) {
            if (!graph.containsKey(edge[0])) graph.put(edge[0], new HashSet<Character>());
            if (!graph.containsKey(edge[1])) graph.put(edge[1], new HashSet<Character>());
            graph.get(edge[0]).add(edge[1]);
            if (!SndIndegree.containsKey(edge[0])) SndIndegree.put(edge[0], 0);
            if (!SndIndegree.containsKey(edge[1])) SndIndegree.put(edge[1], 0);
        }

        Queue<Character> queue = new LinkedList<Character>();
        HashSet<Character> visited = new HashSet<Character>();
        int level = 0;
        queue.offer(tar);
        visited.add(tar);
        int PNum = 1;
        int CNum = 0;
        int maxIndegree = 0;
        char res = '\0';
        while (!queue.isEmpty()) {
            char cur = queue.poll();
            PNum--;
            for (Character neigh : graph.get(cur)) {
                if (level+1 == 2) {
                    if (neigh == tar) continue;
                    int curIndegree = SndIndegree.get(neigh)+1;
                    if (curIndegree > maxIndegree) res = neigh.charValue();
                    SndIndegree.put(neigh, curIndegree);
                }
                else { //not second level
                    if (!visited.contains(neigh)) {
                        queue.offer(neigh);
                        CNum++;
                        visited.add(neigh);
                    }
                }
            }
            if (PNum == 0) {
                PNum = CNum;
                CNum = 0;
                level++;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Solution sol = new Solution();
        char res = sol.recommend('A', new char[][]{{'A','B'},{'A','C'},{'B','D'},{'B','E'},{'C','D'},{'B','A'},{'C','A'}});
        System.out.println(res);
    }
}