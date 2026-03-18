import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/14504
// 버킷 정렬
public class BAEK_14504 {
    static int[] arr;
    static int[][] bucket;
    static int B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        arr = new int[N];
        StringTokenizer stk = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(stk.nextToken());
        }

        B = (int) Math.sqrt(N);
        int bucketCnt = (N + B - 1) / B;
        bucket = new int[bucketCnt][];

        for (int i = 0; i < bucketCnt; i++) {
            int start = i * B;
            int end = Math.min(start + B, N);
            bucket[i] = new int[end - start];
            for (int j = 0; j < bucket[i].length; j++) {
                bucket[i][j] = arr[start + j];
            }
            Arrays.sort(bucket[i]);
        }

        int M = Integer.parseInt(br.readLine());

        for (int m = 0; m < M; m++) {
            stk = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(stk.nextToken());

            if (a == 1) {
                int i = Integer.parseInt(stk.nextToken()) - 1;
                int j = Integer.parseInt(stk.nextToken()) - 1;
                int k = Integer.parseInt(stk.nextToken());
                System.out.println(query(i, j, k));
            } else if (a == 2) {
                int i = Integer.parseInt(stk.nextToken()) - 1;
                int k = Integer.parseInt(stk.nextToken());
                update(i, k);
            }
        }
    }

    static int query(int l, int r, int k) {
        int count = 0;
        int bl = l / B;
        int br = r / B;

        if (bl == br) {
            for (int i = l; i <= r; i++) {
                if (arr[i] > k) {
                    count++;
                }
            }

        } else {
            for (int i = l; i < (bl + 1) * B; i++) {
                if (arr[i] > k) {
                    count++;
                }
            }
            for (int b = bl + 1; b < br; b++) {
                count += getCount(bucket[b], k);
            }

            for (int i = br * B; i <= r; i++) {
                if (arr[i] > k) {
                    count++;
                }
            }
        }
        return count;
    }

    static int getCount(int[] b, int k) {
        int low = 0, high = b.length;
        while (low < high) {
            int mid = (low + high) / 2;
            if (b[mid] <= k) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return b.length - low;
    }

    static void update(int idx, int val) {
        int bIdx = idx / B;
        int oldval = arr[idx];
        arr[idx] = val;

        for (int i = 0; i < bucket[bIdx].length; i++) {
            if (bucket[bIdx][i] == oldval) {
                bucket[bIdx][i] = val;
                break;
            }
        }
        Arrays.sort(bucket[bIdx]);
    }
}
