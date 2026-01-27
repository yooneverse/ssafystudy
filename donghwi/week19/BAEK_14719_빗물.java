import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		int H = Integer.parseInt(stk.nextToken());
		int W = Integer.parseInt(stk.nextToken());
		int result = 0;
		stk = new StringTokenizer(br.readLine());
		ArrayList<Integer> block = new ArrayList<>();
		for(int i=0;i<W;i++) {
			block.add(Integer.parseInt(stk.nextToken()));
		}
		for(int i=1;i<W-1;i++) {
			int wall = block.get(i);
			int LW = wall;
			int RW = wall;
			
			for(int j = i-1;j>=0;j--) {
					LW = Math.max(LW, block.get(j));
			}
			for (int j = i+1;j<W;j++) {
					RW = Math.max(RW,block.get(j));
			}
			if(Math.min(RW, LW) > wall) {
				result += Math.min(LW, RW) - block.get(i);
			}
		}
		System.out.println(result);
	}
}