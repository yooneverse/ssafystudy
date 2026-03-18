
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

// https://www.acmicpc.net/problem/1475
// 구현
public class BAEK_1475 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] c = new char[7];
        c = br.readLine().toCharArray();

        int[] num = new int[10];
        Arrays.fill(num, 0);
        int buy = 0;
        for (int i = 0; i < c.length; i++) {
            int a = (int) c[i] - '0';

            num[a]++;
        }
        int sn = num[6] + num[9];
        num[6] = sn / 2 + sn % 2;
        num[9] = sn / 2 + sn % 2;
        for (int i = 0; i < num.length; i++) {
            buy = Math.max(num[i], buy);
        }
        System.out.println(buy);
    }
}
