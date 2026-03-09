import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/14503
// 구현
public class BAEK_14503 {
    static int N, M;
    static int[][] map;
    static int[] dr = { -1, 0, 1, 0 };
    static int[] dc = { 0, 1, 0, -1 };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stk = new StringTokenizer(br.readLine());
        N = Integer.parseInt(stk.nextToken());
        M = Integer.parseInt(stk.nextToken());
        map = new int[N][M];

        stk = new StringTokenizer(br.readLine());

        int r = Integer.parseInt(stk.nextToken()); // y축 좌표
        int c = Integer.parseInt(stk.nextToken()); // x축 좌표
        int d = Integer.parseInt(stk.nextToken()); // 바라보는 방향 {북: 0,동: 1,남: 2,서: 3}

        for (int i = 0; i < N; i++) {
            stk = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(stk.nextToken());
            }
        }
        BFS(r, c, d);
        System.out.println(search());
    }

    static void BFS(int a, int b, int c) {
        Queue<robot> qu = new LinkedList<>();
        qu.offer(new robot(a, b));

        while (!qu.isEmpty()) {
            robot R = qu.poll();
            if (map[R.a][R.b] == 1) {
                return;
            }
            map[R.a][R.b] = -1;

            for (int d = 0; d < 4; d++) {
                c = c - 1;
                if (c < 0) {
                    c = 3;
                }
                int nr = R.a + dr[c];
                int nc = R.b + dc[c];

                if (map[nr][nc] == 0) {
                    BFS(nr, nc, c);
                    return;
                }
            }
            if (c == 3 || c == 2) {
                qu.offer(new robot(R.a + dr[c - 2], R.b + dc[c - 2]));
            } else {
                qu.offer(new robot(R.a + dr[c + 2], R.b + dc[c + 2]));

            }
        }
    }

    static class robot {
        int a;
        int b;

        robot(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }

    static int search() {
        int count = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == -1) {
                    count++;
                }
            }
        }
        return count;
    }
}
// 계속 직진하면서 닦는게 아니라 무조건 시계 반대방향 90도로 먼저 돌리고 움직인다.