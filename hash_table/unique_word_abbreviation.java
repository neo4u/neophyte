import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public class ValidWordAbbr {
        private final Map<String, Boolean> map = new HashMap<>();
        private final Set<String> set;

        public ValidWordAbbr(String[] words) {
            set = new HashSet<>(Arrays.asList(words));

            for (String s : set) {
                String abbr = toAbbr(s);
                map.put(abbr, !map.containsKey(abbr));
            }
        }

        public boolean isUnique(String word) {
            String abbr = toAbbr(word);
            Boolean hasAbbr = map.get(abbr);
            return hasAbbr == null || (hasAbbr && set.contains(word));
        }

        private String toAbbr(String s) {
            int n = s.length();
            if (n <= 2) {
                return s;
            }
            return s.charAt(0) + Integer.toString(n - 2) + s.charAt(n - 1);
        }
    }
}