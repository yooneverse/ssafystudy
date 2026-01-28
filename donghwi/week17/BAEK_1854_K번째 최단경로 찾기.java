import java.io.*;
import java.util.*;

class Main {
    static int n, m, k;
    // 2차원 그래프 설정
    static List<List<Node>> graph = new ArrayList<>();
    static final int INF = Integer.MAX_VALUE;
    // 우선순위 큐 객체 (정수형) 들을 배열에 집어 넣음
    static PriorityQueue<Integer>[] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stk = new StringTokenizer(br.readLine());

        // 시작점은 1로 고정
        int start = 1;
        n = Integer.parseInt(stk.nextToken());
        m = Integer.parseInt(stk.nextToken());
        k = Integer.parseInt(stk.nextToken());

        // dist 배열 초기화
        dist = new PriorityQueue[n + 1];
        for (int i = 1; i <= n; i++) {
            // 우선순위 큐는 기본적으로 최소 힙
            // 우리는 가장 빠른 경로가 아닌 k번째 경로를 찾아야 함
            // 우선순위 큐를 k개 까지만 담게하고 역순으로 돌리면 (최대 힙) k번째 객체가 나옴!
            dist[i] = new PriorityQueue<>(k, Collections.reverseOrder());
        }

        // graph 배열 초기화
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            stk = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(stk.nextToken());
            int e = Integer.parseInt(stk.nextToken());
            int w = Integer.parseInt(stk.nextToken());
            // graph[시작점]에 도착점과 가중치 정보 넣기 (2차원 배열)
            graph.get(s).add(new Node(e, w));
        }
        // 다익스트라 시작!
        dijkstra(start);

        // 1번에서 시작하여 i번 도로(최종 도착지)의 k번재 최적경로 찾기
        for (int i = 1; i <= n; i++) {
            // 배열에 객체가 k개 보다 작다? -> k번째가 없다.
            if (dist[i].size() < k) {
                // 그런거 없어요
                System.out.println(-1);
            }
            // 있어요?
            else {
                // 최대힙으로 설정해놔서 맨 위를 호출하면 k번째 최단경로가 나와요
                System.out.println(dist[i].peek());
            }
        }

    }

    public static void dijkstra(int start) {
        // 우선순위 큐를 만든다. => (정점, 현재까지의 총 거리) 형태로
        PriorityQueue<Node> pq = new PriorityQueue<>();

        // 시작점에서 시작점의 거리는 0
        dist[start].offer(0);
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {
            // 우선순위 큐 언패킹
            Node current = pq.poll();
            // 현재 도착점
            int current_end = current.end;
            // 현재 가중치
            int current_weight = current.weight;

            // k번째 최단 경로 갱신 로직은 인접 노드 루프 안에서 처리됨.

            // 파이썬의 for i in arr과 같은 구문
            // neighbor(이웃)은 (도착점, 가중치) 형태
            for (Node neighbor : graph.get(current_end)) {

                // 새 거리 = 현재 가중치 + 다음 가중치
                int new_dist = current_weight + neighbor.weight;
                int neighbor_end = neighbor.end;

                // 만약 배열 크기가 k개 보다 작다?
                if (dist[neighbor_end].size() < k) {
                    // 배열에 새 거리를 추가한다.
                    dist[neighbor_end].offer(new_dist);
                    // 다음 while문으로 돌리기 위해 pq에 집어넣는다.
                    pq.offer(new Node(neighbor_end, new_dist));
                }
                // 만약 배열 크기가 k개 이상이고
                // 새 최단거리가 현재 k번째 최단거리보다 짧다?
                else if (new_dist < dist[neighbor_end].peek()) {
                    // 현재 k번재 최단거리 쳐내
                    dist[neighbor_end].poll();
                    // 새로운 최단거리를 집어넣는다.
                    dist[neighbor_end].offer(new_dist);
                    // 다음 while문으로 돌리기 위해 pq에 집어넣는다.
                    pq.offer(new Node(neighbor_end, new_dist));
                }
            }
        }
    }
}

class Node implements Comparable<Node> {
    int end;
    int weight;

    Node(int end, int weight) {
        this.end = end;
        this.weight = weight;
    }

    @Override
    public int compareTo(Node o) {
        return this.weight - o.weight;
    }
}
