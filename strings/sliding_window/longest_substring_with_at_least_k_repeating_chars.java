// Recursive
// 1. Keep a set to store all characters whose frequency is less than k.
// 2. Whenever we encounter a character in this set we call the function recursively to find the longest substring with atleast k repeating characters.
// 3. Exit condition from recursion is when set for that substring is empty meaning all the characters have frequency atleast k.
// 4. At the end one more check is required in case of test case like this cababb and k = 2 
// 5. Source taken from ProgramCreek https://www.programcreek.com/2014/09/leetcode-longest-substring-with-at-least-k-repeating-characters-java/

class Solution{
    public int longestSubstring(String s, int k){
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for(char c : s.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        HashSet<Character> set = new HashSet<>();
        for(char c : map.keySet()){
            if(map.get(c) < k)
                set.add(c);
        }
        if(set.isEmpty()) return s.length();

        int max = 0, begin = 0, end = 0;
        while(end < s.length()){
            char c = s.charAt(end);
            if(set.contains(c)){
                if(end != begin) {
                    max = Math.max(max, longestSubstring(s.substring(begin, end), k));
                }
                begin = end + 1;
            }
            end++;
        }
        if(begin != end)
            max = Math.max(max, longestSubstring(s.substring(begin, end), k));
        return max;
    }
}

class Solution {
    public int longestSubstring(String s, int k) {
        int [] counts = new int[26];
        int max = 0;
        for(int u=1; u<=26;++u){
            Arrays.fill(counts,0);
            int left = 0;
            int right = 0;
            int unique=0;
            int kOrMore = 0;
            while(right<s.length()){
                if(unique<=u){
                    char c = s.charAt(right);
                    int idx = (int)c-(int)'a';
                    counts[idx]++;
                    if(counts[idx]==1){
                        ++unique;
                    }
                    if(counts[idx]==k){
                        ++kOrMore;
                    }
                    ++right;
                }
                else{
                    char o = s.charAt(left);
                    int idx = (int)o-(int)'a';
                    counts[idx]--;
                    if(counts[idx]==0){
                        --unique;
                    }
                    if(counts[idx]==k-1){
                        --kOrMore;
                    }
                    ++left;
                }
                if(unique==u && kOrMore==unique){
                    max=Math.max(max,right-left);
                }
            }
        }
        return max;
    }
}