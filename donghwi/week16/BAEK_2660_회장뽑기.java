import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int INF = 99999999;
		int N = Integer.parseInt(br.readLine());

		int[][] dist = new int[N + 1][N + 1];

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (i != j)
					dist[i][j] = INF;
			}
		}
		String s;
		while (!(s = br.readLine()).equals("-1 -1")) {
			StringTokenizer stk = new StringTokenizer(s);

			int a = Integer.parseInt(stk.nextToken()) - 1;
			int b = Integer.parseInt(stk.nextToken()) - 1;

			dist[a][b] = 1;
			dist[b][a] = 1;
		}

		for (int k = 0; k < N; k++) {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (dist[i][k] + dist[k][j] < dist[i][j]) {
						dist[i][j] = dist[i][k] + dist[k][j];
					}
				}
			}
		}

		int min = INF;

		int[] answer = new int[N];
		for (int i = 0; i < N; i++) {
			int status = 0;
			for (int j = 0; j < N; j++) {
				status = Math.max(status, dist[i][j]);
			}
			answer[i] = status;
			min = Math.min(min, status);
		}

		int cnt = 0;
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < N; i++) {
			if (answer[i] == min) {
				cnt++;
				sb.append((i + 1) + " ");
			}
		}

		System.out.println(min + " " + cnt);
		System.out.println(sb.toString());
	}
}
