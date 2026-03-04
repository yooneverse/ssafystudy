import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/11497
// 그리디 알고리즘
public class BAEK_11497 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		ArrayList<Integer> wood = new ArrayList<>();
		int T = Integer.parseInt(br.readLine());
		int[] result = new int[T];
		for (int i = 0; i < T; i++) {
			int N = Integer.parseInt(br.readLine());
			int[] se = new int[N];
			StringTokenizer stk = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				wood.add(Integer.parseInt(stk.nextToken()));
			}
			Collections.sort(wood);
			int k = 0;
			for (int j = 0; j < N;) {
				se[k] = wood.get(j);
				k++;
				j++;
				if (j == N) {
					break;
				}
				se[N - k] = wood.get(j);
				j++;
			}
			wood.clear();
			int max = 0;
			for (int j = 0; j < N - 1; j++) {
				if (max < Math.abs(se[j] - se[j + 1])) {
					max = Math.abs(se[j] - se[j + 1]);
				}
				result[i] = max;
			}
		}
		for (int i = 0; i < result.length; i++) {
			System.out.println(result[i]);
		}
	}
}