// N개의 정수로 이루어진 배열 A
// 배열 속 정수 순서 적절히 바꿔서
// 연속된 두 수의 차이의 절댓값의 합의 최댓값 구하기
// 3<=N<=8
// 정수 개수 작음. 전체 배열 경우의 수 8! = 40320
// 각 수는 -100 이상 100 이하

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    // main, dfs 함수에서 사용하기 위해 static 변수로 선언
    static int N;   // 총 숫자 개수
    static int[] nums;  // 주어진 숫자 배열
    static int[] picked;    // 뽑은 숫자 배열
    static boolean[] used;  // i번째 숫자 사용 여부
    // 최댓값. 갱신해나갈 것
    static int maxResult = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        nums = new int[N];
        picked = new int[N];
        used = new boolean[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i=0; i<N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        // 가능한 경우 모두 찾기
        dfs(0);
        System.out.println(maxResult);
    }
    // depth : 현재까지 뽑은 숫자의 개수
    static void dfs(int depth) {
        // N개의 숫자를 모두 택했다면 (배열 완성)
        if (depth == N) {
            calculate();
            return;
        }

        for (int i=0; i<N; i++) {
            if (!used[i]) {
                used[i] = true;
                picked[depth] = nums[i];
                // 다음 숫자를 택하러 떠남
                dfs(depth+1);
                used[i] = false;
            }
        }
    }

    static void calculate() {
        int sum = 0;
        for (int i=0; i<N-1; i++) {
            sum += Math.abs(picked[i+1]-picked[i]);
        }
        maxResult = Math.max(maxResult, sum);
    }
}
