import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BAEK_25614 {
    static int N;
    static String M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        StringTokenizer stk = new StringTokenizer(line);

        N = Integer.parseInt(stk.nextToken());
        M = stk.nextToken();

        int[] A = new int[N + 1]; // i번 자리에 있던 회원이 갈 다음 자리
        stk = new StringTokenizer(""); 
        for (int i = 1; i <= N; i++) {
            while (!stk.hasMoreTokens()) {
                stk = new StringTokenizer(br.readLine());
            }
            A[i] = Integer.parseInt(stk.nextToken());
        }

        boolean[] visited = new boolean[N + 1];
        int[] result = new int[N + 1];
        long[] memo = new long[N + 1]; 
        Arrays.fill(memo, -1);

        for (int i = 1; i <= N; i++) {
            if (!visited[i]) {
                ArrayList<Integer> cycle = new ArrayList<>();
                int curr = i;
                while (!visited[curr]) {
                    visited[curr] = true;
                    cycle.add(curr);
                    curr = A[curr];
                }

                int L = cycle.size();
                long move;
                // 동일한 길이의 사이클은 연산 재사용
                if (memo[L] != -1) {
                    move = memo[L];
                } else {
                    move = 0;
                    for (int k = 0; k < M.length(); k++) {
                        move = (move * 10 + (M.charAt(k) - '0')) % L;
                    }
                    memo[L] = move;
                }

                for (int idx = 0; idx < L; idx++) {
                    // startMember: 원래 cycle.get(idx) 자리에 있던 회원 (번호도 cycle.get(idx))
                    int startMember = cycle.get(idx);
                    // move일 뒤에 이 회원이 위치하게 될 사이클 내의 인덱스
                    int targetIdxInCycle = (int) ((idx + move) % L);
                    int finalPos = cycle.get(targetIdxInCycle);
                    
                    // i번 회원의 최종 자리 번호를 저장
                    result[startMember] = finalPos;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            sb.append(result[i]).append(i == N ? "" : " ");
        }
        System.out.println(sb.toString());
    }
}