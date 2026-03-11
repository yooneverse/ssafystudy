import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/1517
// 세그먼트 트리, 분할 정보
// i번째 값의 swap 갯수 -> i 이후의 값들 중 작은 값의 갯수
// 각각 트리를 절반으로 분리하여 각 범위마다 swap 갯수를 세고
// 그 값을 계속 최상위 노드에 더하면 정답이 나온다!
public class BAEK_1517 {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        long[] arr = new long[N];

        StringTokenizer stk = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(stk.nextToken());
        }

        Map<Long, Queue<Integer>> pos = new HashMap<>();
        for (int i = 0; i < N; i++) {
            pos.computeIfAbsent(arr[i], k -> new LinkedList<>()).offer(i);
        }

        long[] index = arr.clone();
        Arrays.sort(index);

        long[] tree = new long[getTreeSize()];
        long ans = 0;
        for (int i = 0; i < N; i++) {
            int idx = pos.get(index[i]).poll();
            ans += sum(tree, 0, N - 1, 1, idx + 1, N - 1);
            update(tree, 0, N - 1, 1, idx, 1);
        }
        System.out.println(ans);
    }

    static int getTreeSize() {
        int h = (int) Math.ceil(Math.log(N) / Math.log(2)) + 1;
        return (int) Math.pow(2, h);
    }

    static long sum(long[] tree, int start, int end, int node, int left, int right) {
        if (end < left || right < start)
            return 0;
        if (left <= start && end <= right) {
            return tree[node];

        }

        int mid = (start + end) / 2;
        return sum(tree, start, mid, node * 2, left, right) + sum(tree, mid + 1, end, node * 2 + 1, left, right);
    }

    static void update(long[] tree, int start, int end, int node, int idx, int dif) {
        if (start == end) {
            tree[node] = dif;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid)
            update(tree, start, mid, node * 2, idx, dif);
        else
            update(tree, mid + 1, end, node * 2 + 1, idx, dif);

        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }
}
