import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        ArrayList<ArrayList<Integer>> tree = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            tree.add(new ArrayList<>());
        }

        for (int i = 0; i < N - 1; i++) {
            StringTokenizer stk = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(stk.nextToken()) - 1;
            int node2 = Integer.parseInt(stk.nextToken()) - 1;
            tree.get(node1).add(node2);
            tree.get(node2).add(node1);
        }

        boolean[] visit = new boolean[N];
        int[] parent = new int[N];

        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        visit[0] = true;
        while (!queue.isEmpty()) {
            int v = queue.remove();
            for (int node : tree.get(v)){
                if (!visit[node]) {
                    visit[node] = true;
                    queue.add(node);
                    parent[node] = v;
                }
            }
        }
        for (int i = 1; i < N; i++) {
            System.out.println(parent[i] + 1);
        }
    }
}