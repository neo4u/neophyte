// Update:

// distance in the follows changed to displacement to avoid confusion:
// see after the code.
// Convert array to string, e.g., [[1,2,3],[4,0,5]] -> "123405",
// hence the corresponding potential swap displacements are: -1, 1, -3, 3.
// Also note, charAt(2) and charAt(3) are not adjacent in original 2
// dimensional int array and therefore are not valid swaps.

class Solution {
    public int slidingPuzzle(int[][] board) {
        Set<String> seen = new HashSet<>(); // used to avoid duplicates
        String target = "123450";
        // convert board to string - initial state.
        String s = Arrays.deepToString(board).replaceAll("\\[|\\]|,|\\s", "");
        Queue<String> q = new LinkedList<>(Arrays.asList(s));
        seen.add(s); // add initial state to set.
        int ans = 0; // record the # of rounds of Breadth Search
        while (!q.isEmpty()) { // Not traverse all states yet?
            // loop used to control search breadth.
            for (int sz = q.size(); sz > 0; --sz) { 
                String str = q.poll();
                if (str.equals(target)) { return ans; } // found target.
                int i = str.indexOf('0'); // locate '0'
                int[] d = { 1, -1, 3, -3 }; // potential swap displacements.
                for (int k = 0; k < 4; ++k) { // traverse all options.
                    int j = i + d[k]; // potential swap index.
                    // conditional used to avoid invalid swaps.
                    if (j < 0 || j > 5 || i == 2 && j == 3 || i == 3 && j == 2) { continue; } 
                    char[] ch = str.toCharArray();
                    // swap ch[i] and ch[j].
                    char tmp = ch[i];
                    ch[i] = ch[j];
                    ch[j] = tmp;
                    s = String.valueOf(ch); // a new candidate state.
                    if (seen.add(s)) { q.offer(s); } //Avoid duplicate.
                }
            }
            ++ans; // finished a round of Breadth Search, plus 1.
        }
        return -1;
    }
}

// Update: 2
// Question: Can you explain how did u determine the potential swap distance?

// Answer:

// When you map a 2 dimensional ( row * column ) matrix to 1 dimensional array, the swap to left and right are still -1 and 1 respectively in terms of index change in 1-D array. In contrast, the swap to up and down are -column and column as of index change.
// That is, for any given index (i, j) in the matrix, it will be mapped to (i * column + j) in the array. Since in the matrix (i, j) could swap with (i, j - 1), (i, j + 1), (i - 1, j), and (i + 1, j), in the array (i * column + j) would swap with (i * column + j - 1), (i * column + j + 1), ((i - 1) * column + j) and ((i + 1) * column + j) accordingly.
// We can easily conclude the swap displacement are -1, 1, -column, and column correspondingly.

// e.g.: Let's consider (1, 2) in the following 3 * 5 matrix

// column # -->               0     1     2     3     4
//                       0  (0,0) (0,1) (0,2) (0,3) (0,4)
//                       1  (1,0) (1,1) (1,2) (1,3) (1,4)
//                       2  (2,0) (2,1) (2,2) (2,3) (2,4)
// we can swap (1, 2) with (1, 1), (1, 3), (0, 2), and (2, 2)

// When mapped to 1 dimensional array, it can be obtained that (1 * 5 + 2) swap with (1 * 5 + 2 - 1), (1 * 5 + 2 + 1), ((1 - 1) * 5 + 2) and ((1 + 1) * 5 + 2):

//   0    1    2    3    4    5    6    7    8    9   10   11   12   13   
// (0,0)(0,1)(0,2)(0,3)(0,4)(1,0)(1,1)(1,2)(1,3)(1,4)(2,0)(2,1)(2,2)(2,3)

//  14
// (2,4)
// Obviously, we can swap 7 with, 6 (= 7 - 1), 8 (= 7 + 1), 2 (= 7 - 5), 12 (= 7 + 5), where 5 is matrix column (width).

// The displacements in the above case are -1, 1, -5, and 5.

// Hope the above answers your question.