// https://www.acmicpc.net/problem/15686

import java.io.*;
import java.util.*;

class BAEK_15686_치킨배달 {
    static int N;
    static int M;
    static int[][] map;
    static ArrayList<Integer> home_y = new ArrayList<>();
    static ArrayList<Integer> home_x = new ArrayList<>();
    static ArrayList<Integer> chicken_y = new ArrayList<>();
    static ArrayList<Integer> chicken_x = new ArrayList<>();
    static boolean[] visited;
    static int result = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stk = new StringTokenizer(br.readLine());
        N = Integer.parseInt(stk.nextToken()); // 도시 크기
        M = Integer.parseInt(stk.nextToken()); // 살아남을 치킨집 갯수
        map = new int[N + 1][N + 1]; 
        for (int i = 1; i <= N; i++) {
            stk = new StringTokenizer(br.readLine());

            for (int j = 1; j <= N; j++) {
                map[i][j] = Integer.parseInt(stk.nextToken());

                if (map[i][j] == 1) {
                    home_y.add(i); // 집 y 좌표
                    home_x.add(j); // 집 x 좌표
                } else if (map[i][j] == 2) {
                    chicken_y.add(i); // 치킨집 y 좌표
                    chicken_x.add(j); // 치킨집 x 좌표
                }
            }
        }
        visited = new boolean[chicken_y.size()]; // 치킨집 선택 여부
        search(0, 0);

        System.out.println(result);
    }

    static void search(int start, int idx) {
        // M만큼 치킨집을 선택했으면
        if (idx == M) {
            // 도시의 치킨 거리 구하기
            int total = calcDistance();
            result = Math.min(result, total);
        }

        for (int i = start; i < chicken_y.size(); i++) {
            visited[i] = true;
            search(i + 1, idx + 1);
            visited[i] = false;
        }
    }

    static int calcDistance() {
        int total = 0;

        for (int i = 0; i < home_y.size(); i++) {
            int hy = home_y.get(i);
            int hx = home_x.get(i);

            int minD = Integer.MAX_VALUE;

            for (int j = 0; j < chicken_y.size(); j++) {
                if (!visited[j]) {
                    continue;
                }

                int cy = chicken_y.get(j);
                int cx = chicken_x.get(j);

                int d = Math.abs(cy - hy) + Math.abs(cx - hx);
                minD = Math.min(minD, d);
            }

            total += minD;
        }
        return total;
    }
}
