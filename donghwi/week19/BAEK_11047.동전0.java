import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter (new OutputStreamWriter(System.out));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		int A, B = 0;
		int N = Integer.parseInt(stk.nextToken());
		int K = Integer.parseInt(stk.nextToken());
		int pr[] = new int [N];
		for(int i=0;i<pr.length;i++) {
			pr[i] = Integer.parseInt(br.readLine());
			
		}Arrays.sort(pr);
		for(int i=pr.length-1;i>=0;i--) {
			A = K%pr[i];
			B += K/pr[i];
			if(A<K) {
				K=A;
			}
		}
		System.out.print(B);
	}

}
