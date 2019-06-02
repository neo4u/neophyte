class Solution {
    public boolean canTransform(String start, String end) {
        int N = start.length();
        char[] S = start.toCharArray(), T = end.toCharArray();
        int i = -1, j = -1;
        while (++i < N && ++j < N) {
            while (i < N && S[i] == 'X')
                i++;
            while (j < N && T[j] == 'X')
                j++;
            /*
             * At this point, i == N or S[i] != 'X', and j == N or T[j] != 'X'. i and j are
             * the indices representing the next occurrences of non-X characters in S and T.
             */

            // If only one of i < N and j < N, then it isn't solid-
            // there's more people in one of the strings.
            if ((i < N) ^ (j < N))
                return false;

            if (i < N && j < N) {
                // If the person isn't the same, it isn't solid.
                // Or, if the person moved backwards, it isn't accessible.
                if (S[i] != T[j] || (S[i] == 'L' && i < j) || (S[i] == 'R' && i > j))
                    return false;
            }
        }
        return true;
    }
}

S: xxxxR
T: xxxxR