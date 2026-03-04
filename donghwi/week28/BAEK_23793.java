import java.io.*;
import java.util.*;

// https://www.acmicpc.net/problem/23793
// 다익스트라 알고리즘
// 주어진 노드와 간선을 통해 최단 경로를 구하는 문제
// 1. X -> Y -> Z의 최단거리
// 2. X -> Z의 최단거리
// 이 두가지를 구한다.

// 기본적으로 다익스트라를 사용하였지만
// ArrayList에 입력값을 저장하면 메모리에 배열이 계속해서 복사되어 느림
// 그래서 Long 변수 하나에 정보(도착지, 가중치)를 비트마스크로 다 때려 넣고
// 원하는 범위만 뽑아내어 사용하는 방식
// 굉장히 빠르지만 혼자서 구현 가능한지 의문
public class BAEK_23793 {
    static final long INF = 1_000_000_007L * 200_000L; // 넉넉하게 잡기

    // 1. 직접 구현한 힙 (최소 힙)
    static long[] heap = new long[400000];
    static int heapSize = 0;

    static void pqPush(long val) {
        heap[++heapSize] = val;
        int current = heapSize;

        while (current > 1 && heap[current] < heap[current / 2]) {
            long temp = heap[current];
            heap[current] = heap[current / 2];
            heap[current / 2] = temp;
            current /= 2;
        }
    }

    static long pqPop() {
        long root = heap[1];
        heap[1] = heap[heapSize--];
        int parent = 1;

        while (parent * 2 <= heapSize) {
            int child = parent * 2;
            if (child + 1 <= heapSize && heap[child + 1] < heap[child]) {
                child++;
            }
            if (heap[parent] <= heap[child])
                break;

            long temp = heap[parent];
            heap[parent] = heap[child];
            heap[child] = temp;
            parent = child;
        }
        return root;
    }

    // 2. 배열 기반 인접 리스트
    static int[] head, next, to, weight;
    static int edgeCount = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        head = new int[N + 1];
        Arrays.fill(head, -1);
        next = new int[M + 1];
        to = new int[M + 1];
        weight = new int[M + 1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            addEdge(u, v, w);
        }

        st = new StringTokenizer(br.readLine());

        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());
        int Z = Integer.parseInt(st.nextToken());

        long[] distFromX = dijkstra(X, N, -1);
        long[] distFromY = dijkstra(Y, N, -1);
        long[] distFromX_noY = dijkstra(X, N, Y);

        long path1 = (distFromX[Y] == INF || distFromY[Z] == INF) ? -1 : distFromX[Y] + distFromY[Z];
        long path2 = (distFromX_noY[Z] == INF) ? -1 : distFromX_noY[Z];

        System.out.println(path1 + " " + path2);
    }

    static long[] dijkstra(int start, int n, int skip) {
        long[] dists = new long[n + 1];
        Arrays.fill(dists, INF);

        heapSize = 0; // pqInit() 효과

        if (start == skip)
            return dists; // 시작점이 스킵 노드면 바로 반환

        dists[start] = 0;
        pqPush((0L << 18) | start);

        while (heapSize > 0) {
            long cur = pqPop();
            long d = cur >> 18;
            int u = (int) (cur & 0x3FFFF);

            if (d > dists[u])
                continue;

            for (int i = head[u]; i != -1; i = next[i]) {
                int v = to[i];
                if (v == skip)
                    continue;

                if (dists[v] > dists[u] + weight[i]) {
                    dists[v] = dists[u] + weight[i];
                    pqPush((dists[v] << 18) | v);
                }
            }
        }
        return dists;
    }

    static void addEdge(int u, int v, int w) {
        to[edgeCount] = v;
        weight[edgeCount] = w;
        next[edgeCount] = head[u];
        head[u] = edgeCount++;
    }
}