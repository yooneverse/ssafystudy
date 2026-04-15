
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BAEK_21940 {
    static int N, M, K;
    static int s, e, w;
    static int[][] dist;
    static int INF = Integer.MAX_VALUE / 2;
    static ArrayList<Integer> X = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stk = new StringTokenizer(br.readLine());
        N = Integer.parseInt(stk.nextToken());
        M = Integer.parseInt(stk.nextToken());

        dist = new int[N + 1][N + 1];
        for (int[] row : dist) {
            Arrays.fill(row, INF);
        }

        for (int i = 1; i <= N; i++) {
            dist[i][i] = 0;
        }
        for (int i = 0; i < M; i++) {
            stk = new StringTokenizer(br.readLine());
            s = Integer.parseInt(stk.nextToken());
            e = Integer.parseInt(stk.nextToken());
            w = Integer.parseInt(stk.nextToken());
            dist[s][e] = Math.min(dist[s][e], w);
        }
        floydWarshall();

        K = Integer.parseInt(br.readLine());
        int[] friends = new int[K];

        stk = new StringTokenizer(br.readLine());

        for (int i = 0; i < K; i++) {
            friends[i] = Integer.parseInt(stk.nextToken());
        }

        int minTime = INF;
        StringBuilder sb = new StringBuilder();

        for (int city = 1; city <= N; city++) {
            int maxRoundTrip = 0;

            for (int i = 0; i < K; i++) {
                int roundTrip = dist[friends[i]][city] + dist[city][friends[i]];
                maxRoundTrip = Math.max(maxRoundTrip, roundTrip); // 친구들 중 최대 왕복시간
            }

            if (maxRoundTrip < minTime) {
                minTime = maxRoundTrip;
                sb = new StringBuilder();
                sb.append(city);
            } else if (maxRoundTrip == minTime) {
                sb.append(" ").append(city); // 동률이면 모두 출력
            }
        }
        System.out.println(sb);
    }
    

    static void floydWarshall() {
        for (int k = 1; k <= N; k++)
            for (int i = 1; i <= N; i++)
                for (int j = 1; j <= N; j++)
                    if (dist[i][k] != INF && dist[k][j] != INF)
                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
    }
}
