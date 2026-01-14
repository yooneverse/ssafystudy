// 각 트럭들은 하나의 단위시간(unit time)에 하나의 단위길이만큼만 이동할 수 있다고 가정한다. 
// 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다.

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 실버_13335_트럭 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();  // 트럭의 수
        int w = sc.nextInt();  // 다리 길이
        int L = sc.nextInt();  // 다리의 최대하중
        int[] truck = new int[n];

        for (int i = 0; i < n; i++) {
            truck[i] = sc.nextInt();
        }

        
        Queue<Integer> q = new LinkedList<>();
        
        // 0으로 채움
        for (int i = 0; i < w; i++) {
            q.offer(0);
        }

        int time = 0;  // 총 시간 
        int total = 0;  // 다리 위 총 무게
        int num = 0;  // 다음 트럭 번호

        while (num < n) {
            time++;  // 1초 경과됨

            // 한 칸 이동함 (맨 앞 제거함)
            total -= q.poll();

            // 트럭이 최대 하중 안 넘으면 올리고,
            // 아니면 0
            if (total + truck[num] <= L) {
                q.offer(truck[num]);   // 트럭 올림
                total += truck[num];   // 무게 증가
                num++;                 // 다음 트럭으로 이동
            } else {
                q.offer(0);  // 못 올리면 빈 칸 추가
            }
        }
        
        time += w;  // 마지막 트럭 다리 건너는 시간 더함
        System.out.println(time);
    }
}
