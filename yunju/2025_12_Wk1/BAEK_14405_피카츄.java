import java.util.Scanner;

public class BAEK_14405_피카츄 {	
	public static boolean solve(String sentence) {

		int len = sentence.length();
		int idx = 0;
		while (idx<len) {
			if ((idx+2<=len)&&(sentence.substring(idx, idx+2).equals("pi")||sentence.substring(idx, idx+2).equals("ka"))) {
				idx += 2;
				continue;
			} else if ((idx+3<=len)&&(sentence.substring(idx,idx+3).equals("chu"))) {
				idx += 3;
				continue;
			}
			return false;
		}
		return true;
	}
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String sentence = sc.next();
		
		if (solve(sentence)) {
			System.out.print("YES");
		} else {
			System.out.print("NO");
		}
	}
}