import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] time = new int[n];
        int[] pay = new int[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer stk = new StringTokenizer(br.readLine());
            time[i] = Integer.parseInt(stk.nextToken());
            pay[i] = Integer.parseInt(stk.nextToken());
        }
        int[] money = new int[n + 1];

        for (int i = 0; i < n; i++) {
            if (i + time[i] <= n) {
                money[i + time[i]] = Math.max(money[i + time[i]], money[i] + pay[i]);
            }
            money[i + 1] = Math.max(money[i + 1], money[i]);
        }
        System.out.println(money[n]);
    }
}