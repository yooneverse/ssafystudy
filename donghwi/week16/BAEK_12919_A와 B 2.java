import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
	static String S;
	static String T;
	static boolean result;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		S = br.readLine();
		T = br.readLine();

		dfs(T);

		if (result) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
	}

	public static void dfs(String t) {
		if (result) {
			return;
		}

		if (t.length() == S.length()) {
			if (t.equals(S)) {
				result = true;
			}
			return;
		}

		char last = t.charAt(t.length() - 1);
		char first = t.charAt(0);

		if (last == 'A') {
			String newt = t.substring(0, t.length() - 1);
			dfs(newt);
		}

		if (first == 'B') {
			StringBuffer sb = new StringBuffer(t);
			String newt = sb.reverse().toString();
			newt = newt.substring(0, t.length() - 1);
			dfs(newt);
		}
	}
}