import java.io.*;
import java.util.*;

class Main {
	static int N;
	static ArrayList<Integer>[] bridge;
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		bridge = new ArrayList[N + 1];

		for (int i = 1; i <= N; i++) {
			bridge[i] = new ArrayList<>();
		}

		for (int i = 0; i < N - 2; i++) {
			StringTokenizer stk = new StringTokenizer(br.readLine());

			int a = Integer.parseInt(stk.nextToken());
			int b = Integer.parseInt(stk.nextToken());

			bridge[a].add(b);
			bridge[b].add(a);
		}
		bfs(1);

		for (int i = 2; i <= N; i++) {
			if (!visited[i]) {
				System.out.println("1 " + i);
				break;
			}
		}
	}

	static void bfs(int start) {
		Queue<Integer> qu = new LinkedList<>();
		visited = new boolean[N + 1];

		qu.add(start);
		visited[start] = true;

		while (!qu.isEmpty()) {
			int local = qu.poll();

			for (int next : bridge[local]) {
				if (!visited[next]) {
					visited[next] = true;
					qu.add(next);
				}
			}
		}
	}
}