Simple version: only output the first valid	

Time: O(n), 2 pass
// Thoughts: According to the idea of ​​judging isValid, as long as you encounter stack<0, it will be removed. After the completion, reverse will come again.
public String removeInvalidParentheses(String s) {
	String r = remove(s, new char[]{'(', ')'});
	String tmp = remove(new StringBuilder(r).reverse().toString(), new char[]{')', '('});
	return new StringBuilder(tmp).reverse().toString();
}
private String remove(String s, char[] p) {
	int stack = 0;
	for (int i = 0; i < s.length(); i++) {
		if (s.charAt(i) == p[0])		stack++;
		if (s.charAt(i) == p[1])		stack--;
		if (stack < 0) {
			s = s.substring(0, i) + s.substring(i + 1);
			i--;
			stack = 0;
		}
	}
	return s;
}
