
import java.util.*;
import java.io.*;

public class Solution {	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		Set<Integer> coinSet = new HashSet<>();
		
		for (int i=0; i<N; i++) {
			int coin = Integer.parseInt(br.readLine());
			if (coin <= K) {
				coinSet.add(coin);
			}
		}
		
		List<Integer> coinList = new ArrayList<>(coinSet);
		Collections.sort(coinList, Collections.reverseOrder());
		
		// dp K(주어질 수 있는 가격)의 최대가 10,000이므로 10,001개로 초기 설정 
		int[] dp = new int[K+1];
		Arrays.fill(dp, 10001);
		dp[0] = 0;
		
		for (int coin : coinList) {
			for (int j=coin; j<=K; j++) {
				dp[j] = Math.min(dp[j], dp[j-coin]+1);
			}
		}
		
		if (dp[K] != 10001) {
			System.out.println(dp[K]);
		} else {
			System.out.println(-1);
		}
	}
}
