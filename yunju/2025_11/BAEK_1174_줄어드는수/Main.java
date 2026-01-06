// N번째 줄어드는 수 구하기
// 포인트 : 줄어드는 수의 개수는 한정적
// 가장 큰 수 : 9876543210 (98억...)
// int 는 +- 21억 
// long을 사용. (int 사용하게 될 시 주의 필요)
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static int N;
    static ArrayList<Long> list = new ArrayList<>();

    public static void dfs(long num) {
        if (!list.contains(num)) {
            list.add(num);
        }

        int last = (int) (num%10);

        for (int i=0; i<last; i++) {
            dfs(num*10+i);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        if (N>1023) {
            System.out.println(-1);
            return;
        }

        for (int i=0; i<10; i++) {
            dfs(i);
        }

        Collections.sort(list);

        System.out.println(list.get(N-1));
    }
}
