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

        // 다리 길이 만큼 한칸 한칸에 무게 (현재는 모두 0) 세팅
        for (int i = 0; i < m; i++) {
            qu.offer(0);
        }
        // 모든 트럭이 지나갈 때 까지 반복
        while (!qu.isEmpty()) {
            // 한 번 움직일 때마다 1++
            time++;
            // 트럭이 다리를 건넜다면
            // => 현재 다리가 버티고 있는 전체 무게 -= 마지막 칸 트럭 무게
            localweight -= qu.poll();
            // 대기중인 트럭이 없을 때 까지 반복
            if (!truck.isEmpty()) {
                // 출발한 트럭 무게 + 현재 하중이 최대 하중보다 작다면
                if (truck.peek() + localweight <= w) {
                    // 트럭 지나가자
                    localweight += truck.peek();
                    qu.offer(truck.poll());
                } else {
                    // 아니면 트럭이 지나가지 못한다.
                    qu.offer(0);
                }
            }

        }
        System.out.println(time);
    }
}