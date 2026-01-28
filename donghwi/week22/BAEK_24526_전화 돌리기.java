
// https://www.acmicpc.net/problem/24526
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main {
    static int N, M;
    static ArrayList<Integer>[] relation;
    static int[] inDegree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stk = new StringTokenizer(br.readLine());

        N = Integer.parseInt(stk.nextToken());
        M = Integer.parseInt(stk.nextToken());

        relation = new ArrayList[N + 1];

        for (int i = 1; i <= N; i++) {
            relation[i] = new ArrayList<>();
        }

        inDegree = new int[N + 1];

        for (int i = 1; i <= M; i++) {
            stk = new StringTokenizer(br.readLine());

            int s = Integer.parseInt(stk.nextToken());
            int e = Integer.parseInt(stk.nextToken());

            relation[e].add(s);
            inDegree[s]++;
        }
        System.out.println(topologySort());
    }

    static int topologySort() {
        Queue<Integer> qu = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            if (inDegree[i] == 0) {
                qu.offer(i);
            }
        }

        int ans = qu.size();

        while (!qu.isEmpty()) {
            Integer cur = qu.peek();
            qu.poll();

            for (int next : relation[cur]) {
                inDegree[next]--;

                if (inDegree[next] == 0) {
                    qu.offer(next);
                    ans++;
                }
            }
        }
        return ans;
    }
}