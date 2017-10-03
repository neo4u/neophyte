    public int numberOfPatterns(int m, int n) {
        boolean[] vis = new boolean[10];
        return dfs(-1, 0, m, n, 0, vis);
    }
    private int dfs(int prev, int len, int m, int n, int cnt, boolean[] vis) {
        if (len >= m && len <= n) ++cnt;
        if (len == n) return cnt;
        if (prev > 0) vis[prev] = true;
        for (int i = 1; i < 10; ++i) {
            if (!vis[i] && isValid(prev, i, vis)) {
                cnt = dfs(i, len + 1, m, n, cnt, vis);
            }
        }
        if (prev > 0) vis[prev] = false;
        return cnt;
    }
    private boolean isValid(int prev, int cur, boolean[] vis) {
        if (prev == -1) return true;
        if (vis[cur]) return false;
        if ((prev + cur) % 2 == 1) return true;
        if (prev + cur == 10) return vis[5];
        if ((prev - 1) % 3 != (cur - 1) % 3 && (prev - 1) / 3 != (cur - 1) / 3) return true;
        return vis[(prev + cur) / 2];
    }