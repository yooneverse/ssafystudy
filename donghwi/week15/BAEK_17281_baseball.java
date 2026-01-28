// https://www.acmicpc.net/problem/17281
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class BAEK_17281_baseball {
    static int N;
    static int max_score = 0;
    static int[][] player;
    static int[] order; // 순서
    static boolean[] selected; // 자리가 있는지 여부

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        player = new int[N + 1][10];
        order = new int[10];
        selected = new boolean[10];

        for (int i = 1; i <= N; i++) {
            StringTokenizer stk = new StringTokenizer(br.readLine());
            for (int j = 1; j <= 9; j++) {
                player[i][j] = Integer.parseInt(stk.nextToken());
            }
        }
        order[4] = 1; // 1번 선수는 무조건 4번 타자
        selected[4] = true; // 4번 자리는 이미 있다는 표시

        recur(2); // 4번 타자는 1번 선수로 정해졌으니 2번 선수부터 시작해서 찾아보자

        System.out.println(max_score);
    }

    static void recur(int num) {
        if (num == 10) {
            baseball();
            return;
        }

        for (int i = 1; i <= 9; i++) {
            if (selected[i]) {
                continue;
            }
            selected[i] = true;
            order[i] = num;
            recur(num + 1);
            selected[i] = false;
        }
    }

    static void baseball() {
        int score = 0;
        int start = 1;
        // 이닝
        for (int i = 1; i <= N; i++) {
            int out = 0;
            boolean flag = false;
            boolean[] base = new boolean[4];

            while (true) {
                if (flag) {
                    break;
                }
                // 야구 선수 순서
                for (int j = start; j <= 9; j++) {
                    int swing = player[i][order[j]];
                    switch (swing) {
                        // 아웃일떄
                        case 0:
                            out++;
                            break;
                        // 안타
                        case 1:
                            for (int k = 3; k >= 1; k--) {
                                if (base[k]) {
                                    if (k == 3) {
                                        score++;
                                        base[3] = false;
                                    } else {
                                        base[k] = false;
                                        base[k + 1] = true;
                                    }

                                }
                            }
                            base[1] = true;
                            break;
                        // 2루타
                        case 2:
                            for (int k = 3; k >= 1; k--) {
                                if (base[k]) {
                                    if (k == 3 || k == 2) {
                                        score++;
                                        base[k] = false;
                                    } else {
                                        base[k] = false;
                                        base[k + 2] = true;
                                    }
                                }
                            }
                            base[2] = true;
                            break;
                        // 3루타
                        case 3:
                            for (int k = 3; k >= 1; k--) {
                                if (base[k]) {
                                    score++;
                                    base[k] = false;
                                }
                            }
                            base[3] = true;
                            break;
                        // 홈런
                        case 4:
                            for (int k = 3; k >= 1; k--) {
                                if (base[k]) {
                                    score++;
                                    base[k] = false;
                                }
                            }
                            score++;
                            break;

                    }
                    if (out == 3) { // 3아웃 되었을 때
                        start = j + 1;

                        if (start == 10) {
                            start = 1;
                        }

                        flag = true;
                        break;
                    }
                }
                if (!flag) {
                    start = 1;
                }
            }
        }
        max_score = Math.max(max_score, score);
    }
}