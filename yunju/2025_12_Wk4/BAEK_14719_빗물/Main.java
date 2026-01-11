// 고이는 빗물의 총량
// 좌우로 높이 체크
// 상승하다가 낮아지게 되는 순간 기준으로 구간 나눔
// 좌우 끝 높이 중 낮은 높이를 기준으로 나머지 높이와의 차이를 누적합

// 일단 맨 왼쪽부터 체크해서 높이가 낮아지는 지점 찾기
// 찾았다면 그 때부터 체크해서 높이가 높아지다 낮아지는 지점 찾기
// 양 끝 중 낮은 높이 기준으로 누적합
// 반복

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        // 버퍼리더
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 한 줄 받아옴. 높이 가로
        String line1 = br.readLine();
        // 읽은 줄을 공백 기준으로 쪼개기 위해 StringTokenizer에 넣어줌
        StringTokenizer st = new StringTokenizer(line1);
        // st 에 있는 쪼개진 문자열을 하나씩 꺼냄
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        int[] heights = new int[W];
        // br은 재사용
        st = new StringTokenizer(br.readLine());

        for (int i=0; i<W; i++) {
            heights[i] = Integer.parseInt(st.nextToken());
        }
        int totalWater = 0;

        // 로직 시작
        // 현재 위치 기준 왼쪽 최대 높이와 오른쪽 최대 높이
        for (int i=1; i<W-1; i++) {
            int leftMax = 0;
            int rightMax =0;

            for (int j=0; j<i; j++) {
                leftMax = Math.max(leftMax, heights[j]);
            }
            for (int j=i+1; j<W; j++) {
                rightMax = Math.max(rightMax, heights[j]);
            }
            // 양 끝 값 중 더 낮은 높이를 기준
            int currentStandard = Math.min(leftMax, rightMax);

            if (currentStandard > heights[i]) {
                totalWater += (currentStandard-heights[i]);
            }
        }
        System.out.print(totalWater);
        br.close();
    }
}