// 키 순서
// N 명의 키가 다른 학생 (2<=N<=500)
// M 번의 비교
// 본인의 키가 몇 번째인지 알 수 있는 학생의 수 출략

// 포인트 : 본인보다 작거나 큰 사람의 수의 총합을 체크
// N-1명이라면 본인의 위치를 알 수 있음

// 특정 두 명의 대소 비교만을 가지고 전체적으로 업데이트를 해야 함
// 플로이드 워셜
// 모든 출발점에서 모든 도착지까지의 길이를 알아낼 수 있음
// 경로? 본 문제에서는 작은 사람에서 큰 사람으로만 경로가 존재한다고 가정

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    // 키가 작은 사람에서 큰 사람으로 경로가 존재하다고 표현
    static boolean[][] connected;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        connected = new boolean[N+1][N+1];
        for (int i = 0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            // a 가 b 보다 작음
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            connected[a][b] = true;
        }

        // 주요 로직: 플로이드 워셜
        // 모든 사람에 대하여 작은 사람에서 큰 사람으로 가는 경로 모두 연결
        for (int k = 1; k <= N; k++) {
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    if (connected[i][k] && connected[k][j]) {
                        connected[i][j] = true;
                    }
                }
            }
        }

        // 결과
        int ans = 0;

        for (int i = 1; i <= N; i++) {
            int know = 0;
            // j번 사람이 i번 사람보다 큰지 작은지 파악 가능한가
            // 같은 사람이면 패스
            for (int j = 1; j <= N; j++) {
                if (i == j) continue;

                if (connected[i][j] || connected[j][i]) {
                    know++;
                }
            }

            if (know == N-1) {
                ans++;
            }
        }
        System.out.println(ans);
    }
}