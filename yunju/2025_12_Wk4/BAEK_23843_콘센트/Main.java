// 전자기기 개수 N, 콘센트 개수 M
// 전자기기 별 충전 필요 시간
// M개의 콘센트에 전자기기 하나씩 넣어주고
// 콘센트 중 가장 짧게 남은 콘센트에 다음 전자기기 넣고?

// 2개 콘센트에 1,2,100 충전한다면 1,100 / 2 가 아니라 1,2 / 100 이 맞다
// 충전 시간 제일 긴 것부터 배정

// 우선순위 큐를 이용

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        long[] times = new long[N];
        for (int i=0; i<N; i++) {
            times[i] = Long.parseLong(st.nextToken());
        }
        // 오름차순 정렬. 가장 마지막 숫자가 가장 큼
        Arrays.sort(times);
        // 우선순위 큐
        PriorityQueue<Long> pq = new PriorityQueue<>();

        // N : 기기 개수
        // M : 콘센트 개수

        // 기본적으로 우선순위 큐는 최소 힙
        // 가장 충전 시간 긴 기기부터 우선순위 큐에 넣어줌
        // 모든 콘센트가 사용 중이라면 그 중 시간이 가장 짧은 콘센트에 넣어줌
        for (int i=N-1; i>=0; i--) {
            if (pq.size() < M) {
                pq.offer(times[i]);
            } else {
                // poll 가장 높은 우선순위 가진 요소를 반환하고 제거
                // 가장 작은 수가 나옴
                // 시간 가장 짧은 콘센트에 다음 충전 시작 
                long minTime = pq.poll();
                pq.offer(minTime+times[i]);
            }
        }
        long maxTime = 0;
        while (!pq.isEmpty()) {
            maxTime = Math.max(maxTime, pq.poll());
        }
        System.out.println(maxTime);
    }
}
// int : +- 21억까지 표현
// long : +- 922경까지 표현 가능
// 위 문제는 N은 최대 10만, 충전 시간 최대 100만
// 1000억까지 나올 수도 있음

