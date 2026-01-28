import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<score> report = new ArrayList<score>();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int D = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());
            report.add(new score(D, W));
        }
        // 내림차 순 정렬
        Collections.sort(report, (o1, o2) -> o2.W - o1.W);

        int time = N;
        int result = 0;

        // 마감일
        for (int i = 0; i < report.size(); i++) {
            if (report.get(i).D >= time) {
                result += report.get(i).W;
                report.remove(i);
                i = -1;
                time--;
            } else if (i == report.size() - 1) {
                i = -1;
                time--;
            }
            if (time == 0) {
                break;
            }
        }
        System.out.println(result);
    }

    public static class score {
        int D;
        int W;

        public score(int D, int W) {
            this.D = D;
            this.W = W;
        }
    }
}