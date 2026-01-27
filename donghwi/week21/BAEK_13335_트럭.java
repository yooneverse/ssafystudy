import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main {
    static int n, m, w;
    static int time = 0;
    static int localweight = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));

        StringTokenizer stk = new StringTokenizer(br.readLine());

        n = Integer.parseInt(stk.nextToken()); // 트럭 갯수
        m = Integer.parseInt(stk.nextToken()); // 다리 길이
        w = Integer.parseInt(stk.nextToken()); // 최대 하중
        Queue<Integer> truck = new LinkedList<>();
        stk = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            truck.offer(Integer.parseInt(stk.nextToken()));
        }

        Queue<Integer> qu = new LinkedList<>();

        for (int i = 0; i < m; i++) {
            qu.offer(0);
        }

        while (!qu.isEmpty()) {
            time++;
            localweight -= qu.poll();
            if (!truck.isEmpty()) {
                if (truck.peek() + localweight <= w) {
                    localweight += truck.peek();
                    qu.offer(truck.poll());
                } else {
                    qu.offer(0);
                }
            }

        }
        System.out.println(time);
    }
}
