
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BAEK_13308 {
    static int N, M;
    static int[] cost;
    static ArrayList<Edge>[] info;

    @SuppressWarnings("unchecked")
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stk = new StringTokenizer(br.readLine());

        N = Integer.parseInt(stk.nextToken());
        M = Integer.parseInt(stk.nextToken());
        cost = new int[N + 1];
        info = new ArrayList[N + 1];
        stk = new StringTokenizer(br.readLine());

        for (int i = 1; i <= N; i++) {
            cost[i] = Integer.parseInt(stk.nextToken());
            info[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            stk = new StringTokenizer(br.readLine());

            int start = Integer.parseInt(stk.nextToken());
            int end = Integer.parseInt(stk.nextToken());
            int weight = Integer.parseInt(stk.nextToken());

            info[start].add(new Edge(end, weight));
            info[end].add(new Edge(start, weight));
        }
        System.out.println(dijkstra());
    }

    public static long dijkstra() {
        long[][] dist = new long[N + 1][2501];

        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= 2500; j++) {
                dist[i][j] = Long.MAX_VALUE;
            }
        }

        PriorityQueue<Node> pq = new PriorityQueue<>();

        pq.add(new Node(1, cost[1], 0));

        while (!pq.isEmpty()) {
            Node curr = pq.poll();

            // 목표 도시 도달 시 리턴
            if (curr.pos == N) {
                return curr.totalOilCost;
            }

            // 이미 더 적은 비용으로 이 도시 + 이 기름값 상태에 도달 한 적 있으면 넘어가기
            if (dist[curr.pos][curr.minOilCost] < curr.totalOilCost) {
                continue;
            }

            for (Edge next : info[curr.pos]) {
                // 다음 도시로 갈 때 드는 비용 = 현재까지의 최소 기름값 * 도로의 길이
                long nextTotalCost = curr.totalOilCost + (long) curr.minOilCost * next.w;
                // 다음 도시에서 갖게 될 최소 기름값 = 현재 기름값 vs 다음 도시 기름값
                int nextMinOil = Math.min(curr.minOilCost, cost[next.v]);

                if (dist[next.v][curr.minOilCost] > nextTotalCost) {
                    dist[next.v][curr.minOilCost] = nextTotalCost;
                    pq.add(new Node(next.v, nextMinOil, nextTotalCost));
                }
            }
        }
        return -1;
    }

    static class Edge {
        int v;
        int w;

        Edge(int e, int w) {
            this.v = e;
            this.w = w;
        }
    }

    static class Node implements Comparable<Node> {
        int pos, minOilCost;
        long totalOilCost;

        Node(int pos, int minOilCost, long totalOilCost) {
            this.pos = pos;
            this.minOilCost = minOilCost;
            this.totalOilCost = totalOilCost;
        }

        @Override
        public int compareTo(Node o) {
            return Long.compare(this.totalOilCost, o.totalOilCost);
        }
    }

}
