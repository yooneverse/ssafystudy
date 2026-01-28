import java.io.*;
import java.util.*;

class Main {
    static int[] guitar;
    static int N;
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stk = new StringTokenizer(br.readLine());

        N = Integer.parseInt(stk.nextToken());
        M = Integer.parseInt(stk.nextToken());
        int left = 0;
        int right = 0;

        guitar = new int[N];

        stk = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            guitar[i] = Integer.parseInt(stk.nextToken());
            right += guitar[i];
            left = Math.max(left, guitar[i]);
        }
        System.out.println(binary(left, right));
    }

    public static int binary(int L, int R) {
        while (L <= R) {
            int total = 0;
            int mid = (L + R) / 2;
            int count = 1;

            for (int i = 0; i < N; i++) {
                total += guitar[i];

                if (total > mid) {
                    total = guitar[i];
                    count++;
                }
            }

            if (count <= M) {
                R = mid - 1;
            } else {
                L = mid + 1;
            }
        }
        return L;
    }
}