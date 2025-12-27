import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class BAEK_20125_쿠키의신체측정 {
    
	public static int[] findHeart(String[] board) {
		int N = board.length;
		
		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++) {
				if (board[i].charAt(j) == '*') {
					int heart_r = i+1;
					int heart_c = j;
					return new int[] {heart_r, heart_c};
				}
			}
		}
		return null;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		String[] board = new String[T];
		
		for (int i=0; i<T; i++) {
			String line = br.readLine();
			board[i] = line;
		}
		int[] heart = findHeart(board);
		int heart_r = heart[0]+1;
		int heart_c = heart[1]+1;
		System.out.println(heart_r + " " + heart_c);
		
		int la=0, ra=0, wa=0, ll=0, rl=0;
		
		// 팔 허리 다리
		for (int i=0; i<T; i++) {
			if (board[heart_r-1].charAt(i) == '*') {
				la = heart_c-i-1;
				break;
			}
		}
		for (int i=T-1; i>=0; i--) {
			if (board[heart_r-1].charAt(i) == '*') {
				ra = i-heart_c+1;
				break;
			}
		}
		int wr =0;
		int wc = 0;
		for (int i=heart_r; i<T; i++) {
			if (board[i].charAt(heart_c-1) == '_') {
				wa = i-heart_r;
				wr = i-1;
				wc = heart_c-1;
				break;
			}
		}
		for (int i=wr+1; i<T; i++) {
			if (board[i].charAt(wc-1) == '_') {
				ll = i - wr-1;
				break;
			}
			ll = T-wr-1;
		}
		for (int i=wr+1; i<T; i++) {
			if (board[i].charAt(wc+1) == '_') {
				rl = i - wr-1;
				break;
			}
			rl = T-wr-1;
		}
		System.out.println(la+" "+ra+" " + wa + " " + ll + " "+ rl);
	}

}
