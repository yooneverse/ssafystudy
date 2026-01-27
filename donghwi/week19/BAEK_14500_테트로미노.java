import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    static int N, M, max = 0;
    static int[][] box;
    static boolean[][] visited;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());

        N = Integer.parseInt(stk.nextToken());
        M = Integer.parseInt(stk.nextToken());

        box = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            stk = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                box[i][j] = Integer.parseInt(stk.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                visited[i][j] = true;
                DFS(i, j, 1, box[i][j]);
                visited[i][j] = false;

                combi(0, 0, i, j, box[i][j]);
            }
        }
        System.out.println(max);
    }

    static void combi(int cnt, int start, int y, int x, int sum) {
        if (cnt == 3) {
            max = Math.max(max, sum);
            return;
        }

        for (int d = start; d < 4; d++) {
            int nr = y + dr[d];
            int nc = x + dc[d];

            if (nr < 0 || nc < 0 || nr >= N || nc >= M) {
                continue;
            }

            combi(cnt + 1, d + 1, y, x, sum + box[nr][nc]);
        }
    }

    static void DFS(int y, int x, int cnt, int sum) {
        if (cnt == 4) {
            max = Math.max(max, sum);
            return;
        }
        for (int d = 0; d < 4; d++) {
            int nr = y + dr[d];
            int nc = x + dc[d];

            if (nr < 0 || nc < 0 || nr >= N || nc >= M) {
                continue;
            }
            if (visited[nr][nc]) {
                continue;
            }

            visited[nr][nc] = true;
            DFS(nr, nc, cnt + 1, sum + box[nr][nc]);
            visited[nr][nc] = false;
        }

    }
}