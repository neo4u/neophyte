# @param {String} s
# @return {String[]}
def remove_invalid_parentheses(s)
    par = ['(', ')']
    ans = []
    dfs(s, 0, 0, ans, par)
    return ans
end

def dfs(s, last_i, last_j, ans, par)
    stack = 0
    for i in (last_i...s.size)
        stack += 1 if s[i] == par[0] 
        stack -= 1 if s[i] == par[1]
        next if stack >= 0
        
        for j in (last_j..i)
            if s[j] == par[1] && (j == last_j || s[j-1] != par[1])
                dfs(s[0...j] + s[j+1...s.size], i, j, ans, par)
            end
        end
        
        return
    end
    
    rev_par = [')', '(']
    reversed = s.reverse
    if par[0] == '('
        dfs(reversed, 0, 0, ans, rev_par)
    else
        ans.push(reversed)
    end
end