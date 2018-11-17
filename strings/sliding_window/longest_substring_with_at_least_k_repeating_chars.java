
// Recursive
// 1. Keep a set to store all characters whose frequency is less than k.
// 2. Whenever we encounter a character in this set we call the function recursively to find the longest substring with atleast k repeating characters.
// 3. Exit condition from recursion is when set for that substring is empty meaning all the characters have frequency atleast k.
// 4. At the end one more check is required in case of test case like this cababb and k = 2 
// 5. Source taken from ProgramCreek https://www.programcreek.com/2014/09/leetcode-longest-substring-with-at-least-k-repeating-characters-java/

public int longestSubstring(String s, int k) {
    HashMap<Character, Integer> map = new HashMap<Character, Integer>();
    for(char c : s.toCharArray()) {
        map.put(c, map.getOrDefault(c, 0) + 1);
    }

    HashSet<Character> set = new HashSet<>();
    for(char c : map.keySet()) {
        if(map.get(c) < k)
            set.add(c);
    }
    if(set.isEmpty()) return s.length();

    int max = 0, begin = 0, end = 0;
    while(end < s.length()) {
        char c = s.charAt(end);
        if(set.contains(c)) {
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



// For each h, apply two pointer technique to find the longest substring
// with at least K repeating characters and
// the number of unique characters in substring is h.

// This might help you to understand the algorithm:
// For h=1:26, we are going to use sliding window (left i, right j)
// to find the "longest window which contains exactly h unique characters
// and for each character, there are at least K repeating ones".
// For example, when h=3, K=5, we are going to find the longest window
// contains exactly 3 unique characters and each repeating 5 times.

public class Solution {
    public int longestSubstring(String s, int k) {
        char[] str = s.toCharArray();
        int[] counts = new int[26];
        int h, i, j, idx, max = 0, unique, noLessThanK;
        
        for (h = 1; h <= 26; h++) {
            Arrays.fill(counts, 0);
            i = 0; 
            j = 0;
            unique = 0;
            noLessThanK = 0;

            while (j < str.length) {
                if (unique <= h) {
                    idx = str[j] - 'a';
                    if (counts[idx] == 0)
                        unique++;
                    counts[idx]++;
                    if (counts[idx] == k)
                        noLessThanK++;
                    j++;
                }
                else {
                    idx = str[i] - 'a';
                    if (counts[idx] == k)
                        noLessThanK--;
                    counts[idx]--;
                    if (counts[idx] == 0)
                        unique--;
                    i++;
                }
                if (unique == h && unique == noLessThanK)
                    max = Math.max(j - i, max);
            }
        }

        return max;
    }
}