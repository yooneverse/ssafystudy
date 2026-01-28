import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

class Main {
    static int N;
    static String[][] birth;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        birth = new String[N][4];
        for (int i = 0; i < N; i++) {
            StringTokenizer stk = new StringTokenizer(br.readLine());

            for (int j = 0; j < 4; j++) {
                birth[i][j] = stk.nextToken();
            }
        }

        Arrays.sort(birth, Comparator
                .comparing((String[] o) -> Integer.parseInt(o[3]))
                .thenComparing(o -> Integer.parseInt(o[2]))
                .thenComparing(o -> Integer.parseInt(o[1])));

        // System.out.println("-------------------------------------");
        // for (int i = 0; i < N; i++) {
        // System.out.println(Arrays.toString(birth[i]));
        // }
        System.out.println(birth[N - 1][0]);
        System.out.println(birth[0][0]);
    }
}