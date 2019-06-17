public int minimumTotal2 (List<List> triangle) {
    int size = triangle.size();
    int[] dp = new int[size];
    dp[0] = triangle.get(0).get(0);

    for(int i=1; i<size; i++){
        List<Integer> list = triangle.get(i);
        int previous = dp[0];
        dp[0] += list.get(0);
        
        //calculating minimum path sum for ith level
        for(int j=1; j<i; j++){
            int temp = dp[j];
            dp[j] = list.get(j) + Math.min(previous, dp[j]);
            previous = temp;
        }
        
        dp[i] = previous + list.get(i);
    }

    int result = dp[0];
    for(int i=1; i<size; i++){
        result = Math.min(result, dp[i]);
    }

    return result;
}

// The idea is to storage the min path sum so far at current level in the array dp[] of max length triangle.size(), then deduce the array values at the next level. When it reaches the triangle.size(), return the minimum of the dp[] array.

public int minimumTotal(List<List<Integer>> triangle) {
        if (triangle.size() == 0)
            return 0;
        if (triangle.size() == 1)
            return triangle.get(0).get(0);

        int[] dp = new int[triangle.size()];
        dp[0] = triangle.get(0).get(0);
        return minimumTotal(triangle, dp, 1);
    }

    public int minimumTotal(List<List<Integer>> triangle, int[] dp, int lvlidx) {
        /**
         * dp: dp[i]_lvlidx = the min path sum up to current level and up to
         * index i
         * 
         * dp[0]_lvlidx = this_level_list[0] + dp[0]_(lvlidx-1);
         * dp[end]_lvlidx = this_level_list[end] + dp[end-1]_(lvlidx-1);
         * 
         * dp[i]_lvlidx = this_level_list[i] + min{ dp[i-1]_(lvlidx-1),
         * dp[i]_(lvlidx-1) };
         */

        List<Integer> list = triangle.get(lvlidx);
        int pre = dp[0], temp;
        dp[0] += list.get(0);
        for (int i = 1; i < lvlidx; i++) {
            temp = dp[i];
            dp[i] = list.get(i) + Math.min(pre, dp[i]);
            pre = temp;
        }
        dp[lvlidx] = pre + list.get(lvlidx);

        if (lvlidx + 1 == triangle.size()) {
            int res = dp[0];
            for (int i = 1; i <= lvlidx; i++)
                res = Math.min(res, dp[i]);
            return res;
        }

        return minimumTotal(triangle, dp, lvlidx + 1);
    }
}