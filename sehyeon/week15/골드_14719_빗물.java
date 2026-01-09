import java.util.Scanner;
import java.util.Arrays;

public class 골드_14719_빗물 {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int H = sc.nextInt(); // 세로
        int W = sc.nextInt(); // 가로
        
        int[] arr = new int[W];

        for (int i = 0; i < W; i++) {
            arr[i] = sc.nextInt();
        }

        // 1. 왼쪽에서 가장 높은 벽 구함 (L)
        // 2. 오른쪽에서 가장 높은 벽 구함 (R)
        // 3. L과 R 중 낮은 높이만큼 물이 참. (min)
        // 4. (min - 현재 내 높이) 만큼 물이 참
        
        for (int i = 1; i < W-1; i++) {
            for (int j = 0; j < W; j++) {
                
            }
        }


    }
}