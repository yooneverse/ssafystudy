import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;

class Main {
    static int N;
    static int[][] map;
    static boolean[][] visited;
    static int count, max, cnt_m;
    static int num = 0;
    static int[] dr = { -1, 0, 1, 0 };
    static int[] dc = { 0, -1, 0, 1 };
    static ArrayList<Integer> arr = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        map = new int[N][N];
        visited = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            char[] s = br.readLine().toCharArray();
            for (int j = 0; j < N; j++) {
                map[i][j] = Character.getNumericValue(s[j]);
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == 1) {
                    BFS(i, j);
                }
            }
        }

        System.out.println(num);
        Collections.sort(arr);
        for (int i = 0; i < num; i++) {
            System.out.println(arr.get(i) - 1);
        }
    }

    static void BFS(int i, int j) {
        Queue<home> qu = new LinkedList<home>();
        count = 2;
        qu.offer(new home(i, j));

        while (!qu.isEmpty()) {
            home h = qu.poll();
            visited[h.a][h.b] = true;
            if (map[h.a][h.b] == 1) {
                num++;
            }

            for (int d = 0; d < 4; d++) {
                int nr = h.a + dr[d];
                int nc = h.b + dc[d];

                if (nr >= 0 && nc >= 0 && nr < N && nc < N) {
                    if (map[nr][nc] == 1 && !visited[nr][nc]) {
                        map[nr][nc] = count++;
                        qu.offer(new home(nr, nc));
                    }
                }
            }
        }
        arr.add(count);
    }

    static class home {
        int a;
        int b;

        home(int a, int b) {
            this.a = a;
            this.b = b;
        }

    }

}