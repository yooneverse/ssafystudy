import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/16235
// 구현
// 각 계절마다 정해진 규칙에 따라 땅에 있는 나무가 변하며 K년 후 살아있는 나무의 갯수를 구하는 문제

// 1. 한 장소에 여러 나무가 있을 수 있다.
// 2. 처음 제공되는 양분은 5이며 모든 땅에 공평하게 있다.
// 3. 봄: 나무가 자신의 나이만큼 양분을 먹고 1살 더 먹는다. 양분이 부족한 나무는 양분을 흡수하기 전에 죽는다.
// 4. 여름: 죽은 나무는 자신의 나이/2 만큼 양분을 공급한다.
// 5. 가을: 나무의 나이가 5의 배수이면 주변 8방향으로 새로운 나무를 생성한다.
// 6. 겨울: 로봇이 입력한 값대로 땅에 양분을 공급한다.
public class BAEK_1625 {
    static int N, M, K;
    static Deque<Integer>[][] tree;
    static int[][] robot;
    static int[][] poop;
    static int[][] newtree;
    static int x, y, z;
    static int[] dr = { -1, -1, -1, 0, 0, 1, 1, 1 };
    static int[] dc = { -1, 0, 1, -1, 1, -1, 0, 1 };

    @SuppressWarnings("unchecked")
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stk = new StringTokenizer(br.readLine());

        N = Integer.parseInt(stk.nextToken()); // 땅크기 N * N
        M = Integer.parseInt(stk.nextToken()); // 처음에 심은 나무 갯수 M
        K = Integer.parseInt(stk.nextToken()); // K년 지난 후 확인

        ArrayList<Integer>[][] tempArr = new ArrayList[N][N];
        tree = new ArrayDeque[N][N];
        robot = new int[N][N];
        poop = new int[N][N];
        newtree = new int[N][N];

        // 로봇이 겨울마다 뿌리는 양분
        for (int i = 0; i < N; i++) {
            stk = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                tree[i][j] = new ArrayDeque<>(); // 나무 배열 초기화 tree[i][j] = {1, 3, 2, ...} 이런 구조
                tempArr[i][j] = new ArrayList<>();
                poop[i][j] = 5; // 처음에 제공되는 양분
                robot[i][j] = Integer.parseInt(stk.nextToken()); // 로봇이 겨울마다 뿌리는 양분
                newtree[i][j] = 0;
            }
        }
        // 나무의 정보
        for (int i = 0; i < M; i++) {
            stk = new StringTokenizer(br.readLine());

            x = Integer.parseInt(stk.nextToken()) - 1; // 나무 x축
            y = Integer.parseInt(stk.nextToken()) - 1; // 나무 y축
            z = Integer.parseInt(stk.nextToken()); // 현재 나무 나이

            // [중요] 세로축이 x!!!!!!!!!!!
            tempArr[x][y].add(z);
        }

        // 어린 나무가 먼저 양분을 먹으니 오름차 순으로 정렬 후 deque에 넣기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!tempArr[i][j].isEmpty()) {
                    Collections.sort(tempArr[i][j]);

                    for (int age : tempArr[i][j]) {
                        tree[i][j].add(age);
                    }
                }
            }
        }

        // K년 동안 사계절 돌리기
        for (int i = 0; i < K; i++) {
            sns();
            authmn();
            winter();
        }
        // 살아있는 나무 갯수 확인 후 출력
        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                result += tree[i][j].size();
            }
        }
        System.out.println(result);
    }

    // 봄, 여름 sns(Spring and Summer)
    static void sns() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                // 다음 세대에 살아남은 나무
                Deque<Integer> nextGen = new ArrayDeque<>();
                if (!tree[i][j].isEmpty()) {
                    // 특정 장소에 있는 나무 갯수만큼 반복문 돌리기
                    int treesize = tree[i][j].size();
                    int dead = 0;
                    for (int k = 0; k < treesize; k++) {
                        int age = tree[i][j].pollFirst();
                        // 양분공급이 가능하면
                        if (poop[i][j] >= age) {
                            poop[i][j] -= age;

                            age++;

                            if (age % 5 == 0) {
                                newtree[i][j]++;
                            }
                            nextGen.addLast(age);

                        } else {
                            // 죽은 나무로 양분 쌓기
                            dead += age / 2;
                            while (!tree[i][j].isEmpty()) {
                                dead += tree[i][j].pollFirst() / 2;
                            }
                            break;
                        }
                    }
                    tree[i][j] = nextGen;
                    // 여름: 죽은 나무들을 양분화
                    poop[i][j] += dead;
                }

            }
        }
    }

    // 가을
    static void authmn() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                // 번식할 나무가 있는 경우만 딱 한 번 진입
                if (newtree[i][j] > 0) {
                    int count = newtree[i][j]; // 번식할 나무 개수 확정
                    for (int d = 0; d < 8; d++) {
                        int nr = i + dr[d];
                        int nc = j + dc[d];

                        if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                            for (int n = 0; n < count; n++) {
                                tree[nr][nc].addFirst(1);
                            }
                        }
                    }
                    newtree[i][j] = 0; // 번식 완료 후 해당 칸 초기화
                }
            }
        }
    }

    static void winter() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                poop[i][j] += robot[i][j];
            }
        }
    }
}
