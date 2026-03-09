import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/3055
// BFS
// 2차원 배열 안에
// 고슴도치(시작 지점), 비버의 굴(도착 지점), 홍수(방해요소), 돌(홍수도 막고 고슴도치도 막음)의 위치가 들어있음
// 1턴 마다 홍수가 주변 4칸에 확장되고 고슴도치는 한 칸 움직일 수 있음
// 고슴도치는 홍수를 피해 비버의 굴로 도착할 수 있는 가장 빠른 시간을 구하는 문제

// 1. 홍수를 BFS로 주변 4칸을 확장한다.
// 2. 고슴도치를 BFS로 주변 4칸을 확장한다.
// 3. 이를 반복하다 확장된 고슴도치가 도착 지점에 도달하면 걸린 시간을 출력한다.
// 4. 만약 고슴도치가 홍수에 막혀 도착 지점에 도달할 수 없다면 "KAKTUS"를 출력한다.
public class BAEK_3055 {
    static int R, C;
    static String[][] matrix;
    static int[] dr = { 0, 1, 0, -1 };
    static int[] dc = { -1, 0, 1, 0 };

    static class hedgehog {
        int a, b;

        hedgehog(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }

    static class water {
        int a, b;

        water(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }

    static Queue<hedgehog> qu = new LinkedList<hedgehog>();
    static Queue<water> wqu = new LinkedList<water>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stk = new StringTokenizer(br.readLine());

        R = Integer.parseInt(stk.nextToken());
        C = Integer.parseInt(stk.nextToken());
        matrix = new String[R][C];
        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                char current = line.charAt(j);
                matrix[i][j] = String.valueOf(current);

                if (current == '*') {
                    wqu.add(new water(i, j));
                } else if (current == 'S') {
                    qu.add(new hedgehog(i, j));
                }
            }
        }
        int result = BFS();
        System.out.println(result == Integer.MAX_VALUE ? "KAKTUS" : result);
    }

    static int BFS() {
        int time = 0;

        while (!qu.isEmpty()) {
            time++;

            int waterSize = wqu.size();
            for (int i = 0; i < waterSize; i++) {
                water cur = wqu.poll();
                for (int d = 0; d < 4; d++) {
                    int nr = dr[d] + cur.a;
                    int nc = dc[d] + cur.b;

                    if (nr >= 0 && nc >= 0 && nr < R && nc < C) {
                        if (matrix[nr][nc].equals(".")) {
                            matrix[nr][nc] = "*";
                            wqu.add(new water(nr, nc));
                        }
                    }
                }
            }

            int hedgeSize = qu.size();
            for (int i = 0; i < hedgeSize; i++) {
                hedgehog cur = qu.poll();
                for (int d = 0; d < 4; d++) {
                    int nr = cur.a + dr[d];
                    int nc = cur.b + dc[d];

                    if (nr >= 0 && nc >= 0 && nr < R && nc < C) {
                        if (matrix[nr][nc].equals("D")) {
                            return time;
                        }
                        if (matrix[nr][nc].equals(".")) {
                            matrix[nr][nc] = "S";
                            qu.add(new hedgehog(nr, nc));
                        }
                    }
                }
            }
        }
        return Integer.MAX_VALUE;
    }
}