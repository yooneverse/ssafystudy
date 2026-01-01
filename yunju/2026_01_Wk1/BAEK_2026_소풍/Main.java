package DFS.BAEK_2026_소풍;

// N 명의 학생 중 K 명의 학생 선택
// 조건: K 명이 모두 친구 관계
// F 개의 친구관계를 주어줌
// K 명 선발이 불가능한 경우 -1 출력

// 포인트 : 가지치기
// K 명이 모두 친구 -> 각자 친구 수가 K-1 명 이상
// 모든 경우의 수를 확인해볼 수 밖에 없음. 
// 한 명씩 K명의 리스트에 넣었다 뺐다 하면서
// 앞 번호부터 확인해서 찾아내는 순간 종료. (System.exit(0))

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int K, N, F;
    static boolean[][] isFriend;
    static int[] friendCnt;
    static ArrayList<Integer> picked = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        K = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        F = Integer.parseInt(st.nextToken());

        isFriend = new boolean[N+1][N+1];
        friendCnt = new int[N+1];

        for (int i=0; i<F; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            isFriend[u][v] = true;
            isFriend[v][u] = true;
            friendCnt[u]++;
            friendCnt[v]++;
        }
        for (int i=1; i<=N; i++) {
            picked.add(i);
            dfs(i);
            picked.remove(picked.size()-1);
        }
        System.out.println(-1);

    }
    static void dfs(int current) {
        if (picked.size() == K) {
            StringBuilder sb = new StringBuilder();
            for (int p : picked) {
                sb.append(p).append("\n");
            }
            System.out.print(sb);
            System.exit(0);
        }
        for (int i = current+1; i <= N; i++) {
            if (friendCnt[i]<K-1) {
                continue;
            }
            if (check(i)) {
                picked.add(i);
                dfs(i);
                picked.remove(picked.size()-1);
            }
        } 
    }
    static boolean check(int target) {
        for (int p : picked) {
            if (!isFriend[target][p]) {
                return false;
            }
        }
        return true;
    }
}
