import java.util.Scanner;
import java.util.Arrays;

public class 골드_2294_동전2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] coin = new int[n];

        for (int i = 0; i < n; i++) {
            coin[i] = sc.nextInt();
        }

        // dp[x] = x원을 만들기 위한 최소 동전 개수
        int[] dp = new int[k + 1];
        
        Arrays.fill(dp, 10001);
        dp[0] = 0;

        for (int i = 0; i < n; i++) {   // 동전 하나씩
            for (int j = coin[i]; j <= k; j++) {    // 금액 증가
                dp[j] = Math.min(dp[j], dp[j - coin[i]] + 1);
            }
        }
        '''
        - dp[j] → 기존 최소 동전 개수
        - dp[j - coin[i]] + 1 → 지금 동전 하나 더 쓴 경우
        
        => 둘 중 최소를 선택
        '''

        if (dp[k] == 10001) {
            System.out.println(-1);
        } else {
            System.out.println(dp[k]);
        }
 
    }
}