import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/1806
// 투 포인터 알고리즘
// 연속된 수들의 부분합 중에 그 합이 S 이상이 된는 것 중, 가장 짧은 것의 길이를 구한다.
// 1. 처음에 두개의 포인트를 같은 지점에 시작하여 두 지점 사이의 숫자들의 합을 구한다.
// 2. 만약 그 범위의 합이 S보다 작으면 오른쪽 포인터를 한 칸 오른쪽으로 옮긴다. (범위가 늘어났다)
// 3. 한 칸 범위가 늘어났으니 숫자들의 합에 한 칸 만큼을 더한다.
// 4. 만약 범위의 합이 S보다 커졌다면 길이를 기록하고, 더 짧은 길이가 나왔다면 갱신한다.
// 5. 그 다음 왼쪽 포인터를 오른쪽으로 한 칸 옮긴다. (범위가 줄어들었다)
// 6. 이 것을 오른쪽 포인터가 N 범위 끝까지 갔다면 멈춘다.
public class BAEK_1806 {
    static int[] arr;
    static int left, right, sum, len, min;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stk = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(stk.nextToken());
        int S = Integer.parseInt(stk.nextToken());

        arr = new int[N + 1];

        stk = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(stk.nextToken());
        }
        left = 0;
        right = 0;
        sum = 0;
        // 최소치 비교를 위한 입력 최댓값
        min = 100_000_001;
        while (right <= N) {

            if (sum >= S) {
                sum -= arr[left++];
                len = right - left + 1;
                if (min > len) {
                    min = len;
                }
            } else if (sum < S) {
                sum += arr[right++];
            }
        }
        System.out.println((min) == 100_000_001 ? 0 : min);
    }
}
