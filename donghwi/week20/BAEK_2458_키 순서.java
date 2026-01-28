import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Main {
    static int N, M;
    // [[], [], [], []] 이런 구조
    static List<ArrayList<Integer>> big, small; 
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stk = new StringTokenizer(br.readLine());
        
        // N : 인구 수
        N = Integer.parseInt(stk.nextToken());
        // M : 키 비교 횟수
        M = Integer.parseInt(stk.nextToken());

        big = new ArrayList<>();
        small = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            // 배열 안에 배열 넣기
            big.add(new ArrayList<>());
            small.add(new ArrayList<>());
        }


        for (int i = 0; i < M; i++) {
            stk = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(stk.nextToken()) - 1;
            int b = Integer.parseInt(stk.nextToken()) - 1;
            big.get(a).add(b);
            small.get(b).add(a);
        }

        int result = 0;
        for (int i = 0; i < N; i++) {
            visited = new boolean[N];
            int bigCount = dfs(i, big) - 1;

            visited = new boolean[N];
            int smallCount = dfs(i, small) - 1;

            if (bigCount + smallCount == N - 1) {
                result ++;
            }
        }
        System.out.println(result);
    }
    static int dfs(int node, List<ArrayList<Integer>> graph) {
        visited[node] = true;
        int count = 1;

        for (int next : graph.get(node)) {
            if (!visited[next]) {
                count += dfs(next, graph);
            }
        }
        return count;
    }
}