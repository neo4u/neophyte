/* SOLUTION 3: dp
    dp[i] represents if substring (0,i) is breakable.
    for each longer substring, we just need to check 
*/
public class Solution3 {
    public boolean wordBreak(String s, Set<String> wordDict) {
        if(s.length() == 0) return false;
        boolean[] breakable = new boolean[s.length() + 1];
        breakable[0] = true;
        for(int i = 1; i <= s.length(); i++){
            for(int j = 0; j < i; j++){
                if(breakable[j] && wordDict.contains(s.substring(j, i))){
                    breakable[i] = true;
                    break;
                }
            }
        }
        //for(boolean b : breakable) System.out.print(b + ", ");
        return breakable[s.length()];
    }
}

// SOLUTION 4: TRIE + MAP
public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        Trie trie = new Trie();
        for(String d : wordDict){
            trie.insert(d);
        }
        List<String> prefix = findPrefix(trie, s);
        Map<String, Boolean> map = new HashMap<String, Boolean>();
        for(String split : prefix){
            if(canBeSplitted(trie, s.replaceFirst(split, ""), map)){
                map.put(split, true);
                return true;
            }
        }
        return false;
    }
    
    private boolean canBeSplitted(Trie root, String input, Map<String, Boolean> map){
        if(map.containsKey(input)) return map.get(input);
        if(root.search(input) || input.length() == 0) return true;
        List<String> prefix = findPrefix(root, input);
        for(String s : prefix){
            String copy = new String(input);
            if(canBeSplitted(root, copy.replaceFirst(s, ""), map)){
                map.put(input, true);
                return true;
            } 
        }
        map.put(input, false);
        return false;
    }
    
    private List<String> findPrefix(Trie root, String input){
        char[] split = input.toCharArray();
        List<String> result = new ArrayList<String>();
        TrieNode pointer = root.root;
        for(int i = 0; i < split.length; i++){
            pointer = pointer.next[split[i] - 'a'];
            if(pointer == null) break;
            if(pointer.word != null) result.add(pointer.word);
        }
        return result;
    }    

    class TrieNode {
    
        public String word;
        public TrieNode[] next;
        public TrieNode() {
            word = null;
            next = new TrieNode[26];
        }
    }

    public class Trie {
        private TrieNode root;
    
        public Trie() {
            root = new TrieNode();
        }
    
        public void insert(String word) {
            TrieNode pointer = root;
            for(int i = 0; i < word.length(); i++){
                if(pointer.next[word.charAt(i) - 'a'] == null){
                    pointer.next[word.charAt(i) - 'a'] = new TrieNode();
                }
                pointer = pointer.next[word.charAt(i) - 'a'];
            }
            pointer.word = word;
        }
    
        public boolean search(String word) {
            TrieNode pointer = root;
            if(root.word != null && root.word.equals(word)) return true;
            for(int i = 0; i < word.length(); i++){
                if(pointer.next[word.charAt(i) - 'a'] == null) return false;
                pointer = pointer.next[word.charAt(i) - 'a'];
            }
            if(pointer.word == null) return false;
            return pointer.word.equals(word);
        }
    }
}