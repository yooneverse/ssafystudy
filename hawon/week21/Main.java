import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 학생 수
        int N = Integer.parseInt(br.readLine());

        // 첫 번째 학생이 기준
        StringTokenizer st = new StringTokenizer(br.readLine());
        String oldName = st.nextToken();
        int oldD = Integer.parseInt(st.nextToken());
        int oldM = Integer.parseInt(st.nextToken());
        int oldY = Integer.parseInt(st.nextToken());

        String youngName = oldName;
        int youngD = oldD;
        int youngM = oldM;
        int youngY = oldY;

        // 나머지 돌기
        for (int i = 1; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int d = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            // 늙은놈 찾기
            if (y < oldY) {
                // 연도가 더 빠르면 바로 교체
                oldName = name; oldD = d; oldM = m; oldY = y;
            } else if (y == oldY) {
                // 연도 같으면 월 비교
                if (m < oldM) {
                    oldName = name; oldD = d; oldM = m; oldY = y;
                } else if (m == oldM) {
                    // 월도 같으면 일 비교
                    if (d < oldD) {
                        oldName = name; oldD = d; oldM = m; oldY = y;
                    }
                }
            }

            // 젊은놈 찾기
            if (y > youngY) {
                // 연도가 더 크면 바로 교체
                youngName = name; youngD = d; youngM = m; youngY = y;
            } else if (y == youngY) {
                // 연도 같으면 월 비교
                if (m > youngM) {
                    youngName = name; youngD = d; youngM = m; youngY = y;
                } else if (m == youngM) {
                    // 월도 같으면 일 비교
                    if (d > youngD) {
                        youngName = name; youngD = d; youngM = m; youngY = y;
                    }
                }
            }
        }

        System.out.println(youngName);
        System.out.println(oldName);
    }
}