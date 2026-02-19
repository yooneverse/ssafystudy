
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> arr = new ArrayList<>();
        StringTokenizer stk;

        stk = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(stk.nextToken());
        int x = Integer.parseInt(stk.nextToken());

        stk = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            int person = Integer.parseInt(stk.nextToken());
            arr.add(person);
        }

        int sum = 0;
        for (int i = 0; i < x; i++) {
            sum += arr.get(i);
        }

        int cnt = 1;
        int max = sum;
        for (int i = x; i < n; i++) {
            sum += arr.get(i) - arr.get(i - x);

            if (max == sum) {
                cnt++;
            } else if (sum > max) {
                max = sum;
                cnt = 1;
            }

        }

        if (max == 0) {
            System.out.println("SAD");
            return;
        }
        System.out.println(max);
        System.out.println(cnt);
    }
}