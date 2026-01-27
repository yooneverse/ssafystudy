
// https://www.acmicpc.net/problem/15918
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    static int count = 0;
    static int n, x, y;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stk = new StringTokenizer(br.readLine());

        n = Integer.parseInt(stk.nextToken());
        x = Integer.parseInt(stk.nextToken());
        y = Integer.parseInt(stk.nextToken());

        int[] arr = new int[n * 2 + 1];
        boolean[] visited = new boolean[n + 1];

        int fixedValue = y - x - 1;
        arr[x] = fixedValue;
        arr[y] = fixedValue;
        visited[fixedValue] = true;

        solve(1, arr, visited);

        System.out.println(count);
    }

    static void solve(int idx, int[] arr, boolean[] visited) {
        // 모든 칸을 다 검사했다면 성공
        if (idx == 2 * n + 1) {
            count++;
            return;
        }

        if (arr[idx] != 0) {
            // 이미 숫자가 채워져 있는 칸(고정값 등)이라면 다음 칸으로 패스
            solve(idx + 1, arr, visited);
        } else {
            // 비어있는 칸이라면 어떤 숫자를 넣을지 결정
            for (int i = 1; i <= n; i++) {

                // 이미 사용한 숫자는 건너뜀 (가지치기)
                if (visited[i])
                    continue;

                // 숫자 i를 넣었을 때 짝꿍 i가 들어갈 위치 계산
                int nextPos = idx + i + 1;

                // 짝꿍 자리가 배열 범위 안이고, 그 자리도 비어있다면?
                if (nextPos <= 2 * n && arr[nextPos] == 0) {
                    // 두 곳에 숫자를 넣는다.
                    arr[idx] = arr[nextPos] = i;
                    visited[i] = true;

                    // 다음 단계로
                    solve(idx + 1, arr, visited); 

                    // 백트래킹 (원상복구)
                    arr[idx] = arr[nextPos] = 0;
                    visited[i] = false;
                }
            }
        }
    }
}