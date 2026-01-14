// https://www.acmicpc.net/problem/11657
import java.io.*;
import java.util.*;

public class BAEK_11657_타임머신 {
    static int n;                  // 정점(노드)의 개수
    static int m;                  // 간선(도로)의 개수
    static int[][] graph;          // 간선 정보를 저장할 배열 [출발, 도착, 가중치]
    static long[] distance;        // 시작점으로부터의 최단 거리 배열
    static final int INF = 2000000000; // 도달할 수 없는 노드를 표현하기 위한 큰 값 (무한대 역할)

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 첫 줄 입력: n(노드 수), m(간선 수)
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = Integer.parseInt(stk.nextToken());
        m = Integer.parseInt(stk.nextToken());

        graph = new int[m][3];   // 간선 개수 m만큼 3칸짜리 배열 생성 (출발, 도착, 비용)
        distance = new long[n + 1]; // 1번 노드부터 시작하므로 n+1 크기로 생성

        // 간선 정보 입력 받기
        for (int i = 0; i < m; i++) {
            stk = new StringTokenizer(br.readLine());
            graph[i][0] = Integer.parseInt(stk.nextToken()); // 출발 노드
            graph[i][1] = Integer.parseInt(stk.nextToken()); // 도착 노드
            graph[i][2] = Integer.parseInt(stk.nextToken()); // 이동 비용(가중치)
        }

        StringBuilder sb = new StringBuilder();

        // 벨만-포드 알고리즘 수행
        // 반환값이 true이면 음수 사이클 존재 → -1 출력
        if (bellmanFord(1)) {
            sb.append(-1);
        } else {
            // 1번 노드를 제외한 나머지 노드까지의 거리 출력
            for (int i = 2; i <= n; i++) {
                // 도달할 수 없는 경우 -1, 도달 가능한 경우 거리 출력
                long result = distance[i] == INF ? -1 : distance[i];
                sb.append(result).append("\n");
            }
        }

        System.out.println(sb);
    }

    // 벨만-포드 알고리즘 구현 메서드
    static boolean bellmanFord(int start) {
        // 모든 거리를 무한대로 초기화
        Arrays.fill(distance, INF);
        // 시작 노드의 거리는 0으로 설정
        distance[start] = 0;

        // (n - 1)번 반복: 모든 간선을 확인하며 최단 거리 갱신
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < m; j++) {
                int from = graph[j][0];  // 출발 노드
                int to = graph[j][1];    // 도착 노드
                int cost = graph[j][2];  // 간선 가중치

                // 출발 노드가 아직 도달 불가능 상태가 아니라면
                if (distance[from] != INF) {
                    // 더 짧은 경로가 발견되면 갱신
                    distance[to] = Math.min(distance[to], distance[from] + cost);
                }
            }
        }

        // 마지막 한 번 더 검사해서 음수 사이클 존재 여부 확인
        boolean Cycle = false;
        for (int i = 0; i < m; i++) {
            int from = graph[i][0];
            int to = graph[i][1];
            int cost = graph[i][2];

            // 만약 더 짧은 경로가 발견된다면 → 음수 사이클 존재
            if (distance[from] != INF && distance[to] > distance[from] + cost) {
                Cycle = true;
                break;
            }
        }

        // 음수 사이클이 있으면 true, 없으면 false 반환
        return Cycle;
    }
}
