
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/14003
// 이진 탐색, 역추적
class BAEK_14003 {
    static int[] arr;
    static int[] lis;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        arr = new int[N];
        StringTokenizer stk = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(stk.nextToken());
        }

        lis = new int[N + 1];

        lis[0] = -1_000_000_001;
        int[] dp = new int[N];
        int len = 0;
        int idx = 0;

        for (int i = 0; i < N; i++) {
            if (arr[i] > lis[len]) {
                dp[i] = ++len;
                lis[len] = arr[i];
            } else {
                idx = binarySearch(0, len, arr[i]);
                lis[idx] = arr[i];
                dp[i] = idx;
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append(len + "\n");

        Stack<Integer> result = new Stack<>();

        for (int i = N - 1; i >= 0; i--) {
            if (dp[i] == len) {
                result.push(arr[i]);
                len--;
            }
        }

        while (!result.isEmpty()) {
            sb.append(result.pop() + " ");
        }
        System.out.println(sb.toString());
    }

    static int binarySearch(int left, int right, int key) {
        int mid = 0;
        while (left < right) {
            mid = (left + right) / 2;

            if (lis[mid] < key) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return right;
    }
}
