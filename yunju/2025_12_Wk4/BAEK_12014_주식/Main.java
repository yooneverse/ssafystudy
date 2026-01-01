// N 일간의 주식 가격
// K 번 구매 (K 일)
// 직전 주식 구매 가격보다 올랐을 때만 구매
// 즉, 증가하는 부분 수열
// 주식 구매 가능 여부를 판단
// 최장 증가하는 수열의 길이가 K 이상인가

// N <= 10000
// DP는 본인 기준 앞의 모든 숫자들을 비교해야 함 O(N^2)
// 이분탐색 O(NlogN)
// 길이가 중요 >> 수열의 마지막 값만 관리

// 주안점 새로운 숫자를 어떻게 처리할 것인가
// 현재 최장 수열의 끝값보다 크다면 뒤에 붙여주고
// !!! 아니라면 해당 숫자보다 처음으로 큰 숫자와 교체 !!!
// 수열의 길이는 유지하면서 미래 가능성을 붙여줌
// 숫자가 들어갈 자리를 찾는 방식: 이분 탐색
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int tc=1; tc<=T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            int[] prices = new int[N];

            st = new StringTokenizer(br.readLine());

            for (int i=0;i<N;i++) {
                prices[i] = Integer.parseInt(st.nextToken());
            }

            // 알고리즘
            // 길이 계산용 배열
            int[] lisArr = new int[N];
            int len = 0;
            // prices 배열 속 값들
            for (int price : prices) {
                // 만약 수열에 숫자가 없거나, 마지막 값보다 새가격이 크다면 추가
                if (len == 0 || price > lisArr[len-1]) {
                    lisArr[len++] = price;
                }
                // 그게 아니라면 price가 들어갈 자리를 찾아서 교체
                else {
                    int idx = lowerBound(lisArr, len, price);
                    lisArr[idx] = price;
                }
            }
            // 결과 출력 위한 StringBuilder 사용
            sb.append("Case #").append(tc).append("\n");
            if (len >= K) {
                sb.append(1).append("\n");
            } else {
                sb.append(0).append("\n");
            }
        }
        System.out.print(sb);
    }
    // 길이가 size인 arr에서 target이 들어갈 위치 찾기
    // 이분 탐색
    private static int lowerBound(int[] arr, int size, int target) {
        int left = 0;
        int right = size;

        while (left < right) {
            int mid = (left+right) / 2;

            if (arr[mid] >= target) {
                right = mid;
            }
            else {
                left = mid+1;
            }
        }
        return left;
    }
}

// StringBuilder 문자열 도구 (여러 테스트 케이스 출력 시 시간 아껴줌)
// String은 불변, StringBuilder은 가변
// String은 +로 합치면 매번 메모리 복사 일어나 느림
// StringBuilder는 메모리에 모아뒀다가 마지막에 한 번만 출력 빠름


// 데이터 입력 과정
// System.in으로 비트로 들어옴
// InputStreamReader가 비트를 문자로 바꿔줌. 하나씩 하나씩
// BufferedReader가 하나씩 들어온 문자를 모아뒀다가 (임시저장소) 통째로 가져옴
// StringTokenizer는 버퍼리더가 통째로 가져온 문자열을 잘라서 사용하게 해줌