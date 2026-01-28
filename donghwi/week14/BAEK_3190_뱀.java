import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

class Main {
    static int n, d = 0;
    static int[][] map;
    static Map<Integer, String> moveInfo;
    static int[] dx = { 1, 0, -1, 0 };
    static int[] dy = { 0, 1, 0, -1 };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = null;

        n = Integer.parseInt(br.readLine());
        map = new int[n][n];
        moveInfo = new HashMap<>();

        int k = Integer.parseInt(br.readLine());

        for (int i = 0; i < k; i++) {
            stk = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(stk.nextToken());
            int b = Integer.parseInt(stk.nextToken());
            map[a - 1][b - 1] = 1;
        }

        int L = Integer.parseInt(br.readLine());
        for (int i = 0; i < L; i++) {
            stk = new StringTokenizer(br.readLine());

            int time = Integer.parseInt(stk.nextToken());
            String dir = stk.nextToken();
            moveInfo.put(time, dir);
        }

        solve();
    }

    static void solve() {
        Queue<Integer> qu = new LinkedList<>();
        qu.add(0);
        int time = 0;
        int px = 0;
        int py = 0;

        while (true) {
            int nx = px + dx[d];
            int ny = py + dy[d];
            time++;

            if (nx < 0 || ny < 0 || nx > n - 1 || ny > n - 1) {
                break;
            }

            if (qu.contains(ny * n + nx)) {
                break;
            }

            if (map[ny][nx] == 1) {
                map[ny][nx] = 0;
                qu.add(ny * n + nx);
            } else {
                qu.add(ny * n + nx);
                qu.poll();
            }

            if (moveInfo.containsKey(time)) {
                String data = moveInfo.get(time);

                if (data.equals("D")) {
                    d++;
                    if (d == 4)
                        d = 0;
                } else {
                    d--;
                    if (d == -1)
                        d = 3;
                }
            }
            px = nx;
            py = ny;
        }
        System.out.println(time);
    }
}