import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력 1줄: n(트럭 수), w(다리 길이), l(최대 하중)
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        // 입력 2줄: 트럭 무게들
        int[] trucks = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            trucks[i] = Integer.parseInt(st.nextToken());
        }

        // java에서 큐 선언할 때 하는 거
        ArrayDeque<Integer> bridge = new ArrayDeque<>();

        // q를 다 0으로 채우기
        for (int i = 0; i < w; i++) bridge.addLast(0);

        int time = 0;          // 전체 시간(초)
        int nowWeight = 0;     // 현재 다리 위 총 무게
        int idx = 0;           // 아직 안 올라간 트럭의 인덱스

        // 아직 트럭이 남아있거나, 다리 위에 트럭이 남아있으면 계속 진행
        while (idx < n || nowWeight > 0) {
            time++;

            // 1초 지남 -> 다리 맨 앞 칸이 빠짐
            int out = bridge.pollFirst();
            nowWeight -= out;

            // 다음 트럭이 올라갈 수 있으면 올라감, 아니면 0 넣어서 시간만 흐르게 함
            if (idx < n && nowWeight + trucks[idx] <= l) {
                bridge.addLast(trucks[idx]);
                nowWeight += trucks[idx];
                idx++;
            } else {
                bridge.addLast(0);
            }
        }

        System.out.println(time);
    }
}
