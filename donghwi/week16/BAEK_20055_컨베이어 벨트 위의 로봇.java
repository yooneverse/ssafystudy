import java.io.*;
import java.util.*;

class Main {
	static int next;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer stk = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(stk.nextToken());
		int K = Integer.parseInt(stk.nextToken());

		int[] belt = new int[N * 2];
		boolean[] robot = new boolean[N];

		stk = new StringTokenizer(br.readLine());

		for (int i = 0; i < belt.length; i++) {
			belt[i] = Integer.parseInt(stk.nextToken());
		}
		int cnt = 0;
		boolean run = true;

		while (run) {
			cnt++;

			int temp = belt[0];
			boolean b_temp = robot[0];

			belt[0] = belt[N * 2 - 1];

			for (int i = N * 2 - 2; i >= 0; i--) {
				belt[i + 1] = belt[i];
			}
			belt[1] = temp;

			for (int i = N - 1; i > 0; i--) {
				robot[i] = robot[i - 1];
			}
			robot[0] = false;
			robot[N - 1] = false;

			for (int i = N - 1; i > 0; i--) {
				if (robot[i - 1] && !robot[i] && belt[i] >= 1) {
					belt[i]--;
					robot[i] = true;
					robot[i - 1] = false;
				}
			}

			if (belt[0] > 0 && robot[0] == false) {
				belt[0]--;
				robot[0] = true;
			}

			int down = 0;
			for (int i = 0; i < belt.length; i++) {
				if (belt[i] == 0) {
					down++;
				}
			}
			if (down >= K) {
				run = false;
			}
		}
		System.out.println(cnt);
	}
}
