import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    static int[][] board;
    static int result;
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        board = new int[n][n];
        result = 0;

        for (int i = 0; i < n; i++) {
            StringTokenizer stk = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(stk.nextToken());
            }
        }
        run(0);
        System.out.println(result);
    }

    public static void run(int count) {
        if (count == 5) {
            findmax();
            return;
        }
        int copy[][] = new int[n][n];
        for (int i = 0; i < n; i++) {
            copy[i] = board[i].clone();
        }
        for (int i = 0; i < 4; i++) {
            move(i);
            run(count + 1);
            for (int j = 0; j < n; j++) {
                board[j] = copy[j].clone();
            }
        }
    }

    public static void move(int dir) {
        switch (dir) {
            // 위
            case 0:
                for (int i = 0; i < n; i++) {
                    int block = 0;
                    int index = 0;
                    for (int j = 0; j < n; j++) {
                        if (board[j][i] != 0) {
                            if (block == board[j][i]) {
                                board[index - 1][i] = block * 2;
                                block = 0;
                                board[j][i] = 0;
                            } else {
                                block = board[j][i];
                                board[j][i] = 0;
                                board[index][i] = block;
                                index++;
                            }
                        }
                    }
                }
                break;
            // 아래
            case 1:
                for (int i = 0; i < n; i++) {
                    int block = 0;
                    int index = n - 1;
                    for (int j = n - 1; j >= 0; j--) {
                        if (board[j][i] != 0) {
                            if (block == board[j][i]) {
                                board[index + 1][i] = block * 2;
                                block = 0;
                                board[j][i] = 0;
                            } else {
                                block = board[j][i];
                                board[j][i] = 0;
                                board[index][i] = block;
                                index--;
                            }
                        }
                    }
                }
                break;
            // 왼쪽
            case 2:
                for (int i = 0; i < n; i++) {
                    int block = 0;
                    int index = 0;
                    for (int j = 0; j < n; j++) {
                        if (board[i][j] != 0) {
                            if (block == board[i][j]) {
                                board[i][index - 1] = block * 2;
                                block = 0;
                                board[i][j] = 0;
                            } else {
                                block = board[i][j];
                                board[i][j] = 0;
                                board[i][index] = block;
                                index++;
                            }
                        }
                    }
                }
                break;
            // 오른쪽
            case 3:
                for (int i = 0; i < n; i++) {
                    int block = 0;
                    int index = n - 1;
                    for (int j = n - 1; j >= 0; j--) {
                        if (board[i][j] != 0) {
                            if (block == board[i][j]) {
                                board[i][index + 1] = block * 2;
                                board[i][j] = 0;
                                block = 0;
                            } else {
                                block = board[i][j];
                                board[i][j] = 0;
                                board[i][index] = block;
                                index--;
                            }
                        }
                    }
                }
                break;
        }
    }

    public static void findmax() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result = Math.max(result, board[i][j]);
            }
        }
    }
}