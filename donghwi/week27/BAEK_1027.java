import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/1027
// 브루트포스 알고리즘
public class BAEK_1027 {
    static int N;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        StringTokenizer stk = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(stk.nextToken());
        }
        int ans = 0;

        for (int i = 0; i < N; i++) {
            double slope = 1000000001.0;
            int cnt = 0;

            for (int j = i - 1; j >= 0; j--) {
                double cur_slope = calculateSlope(i, j, arr[i], arr[j]);
                if (cur_slope >= slope) {
                    continue;
                }
                cnt++;
                slope = cur_slope;
            }
            slope = -1000000001.0;

            for (int j = i + 1; j < N; j++) {
                double cur_slope = calculateSlope(i, j, arr[i], arr[j]);
                if (cur_slope <= slope) {
                    continue;
                }
                cnt++;
                slope = cur_slope;
            }
            ans = Math.max(ans, cnt);
        }
        System.out.println(ans);
    }

    /**
     * 두 점 (x1, y1)과 (x2, y2) 사이의 기울기를 구하는 메서드
     * 공식: (y2 - y1) / (x2 - x1)
     */
    private static double calculateSlope(int x1, int x2, int y1, int y2) {
        return ((double) y2 - (double) y1) / ((double) x2 - (double) x1);
    }
}
