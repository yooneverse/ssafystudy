package DP.BAEK_2533_사회망서비스;
// 트리 형태
// 아이디어를 받아들이는 조건: 본인의 모든 친구가 얼리아답터
// 최소의 얼리 아답터를 확보하여 모든 사람이 아이디어를 받아들이도록
// 최소 얼리아답터의 수를 출력

// dp 아이디어
// 작은 문제로 나누어보자
// 부모가 얼리어답터인 경우 -> 자식은 노상관
// 부모가 얼리어답터 아닌 경우 -> 자식 무조건 얼리아답터

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
    static int N;
    static ArrayList<Integer>[] adj;
    static int[][] dp;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        // 연결리스트 adj
        // 트리의 연결 상태를 등록
        adj = new ArrayList[N+1];
        // 경우별 필요한 어답터 수
        dp = new int[N+1][2];
        // 노드 계산 여부 (부모자식이 아니라 친구관계로 주어졌기 때문에 중복 계산 방지)
        visited = new boolean[N+1];

        // 각 노드별로 인접 노드 넣을 객체 생성
        for (int i=1; i<=N; i++) {
            adj[i] = new ArrayList<>();
        }
        // 트리 구조 입력
        for (int i=0; i<N-1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            adj[u].add(v);
            adj[v].add(u);
        }
        dfs(1);
        System.out.println(Math.min(dp[1][0], dp[1][1]));
    }


    // dp 의 아이디어
    // 리프 노드는 자식이 없음. 본인의 선택에 따라 얼리아답터 개수 정해짐
    // 리프 노드의 부모는?
    // 본인이 얼리아답터 아니면 모든 자식이 얼리아답터 >> dp[부모][0] = dp[자식][1] 들의 합
    // 본인이 얼리어답터면 자식은 상관 없음. min(dp[자식][0], dp[자식][1])들의 합
    static void dfs(int u) {
        visited[u] = true;
        // u가 얼리어답터가 아닌 경우
        dp[u][0] = 0;
        // u가 얼리어답터인 경우
        dp[u][1] = 1;

        // u의 자식 노드들에 대하여
        for (int v : adj[u]) {
            if (!visited[v]) {
                // 자식부터 올라오면서 계산 (리프노드부터)
                dfs(v);
                // u가 얼리어답터가 아닌 경우 모든 v가 얼리어답터여야 함
                dp[u][0] += dp[v][1];
                // u가 얼리어답터라면 v는 상관없음. 최소를 택함.
                dp[u][1] += Math.min(dp[v][0], dp[v][1]);
            }
        }
    }
}

// static 변수 : 클래스 변수
// 이 클래스로 만든 모든 객체가 공유
// 프로그램 시작 시 하나 만들어짐. 객체 만들지 않아도 사용 가능
// static String name = " ";

// 인스턴스 변수
// 객체마다 따로따로 가짐. new 사용해서 객체 만들 때마다 생김
// String name;

// 지역 변수 : 메서드 안에 선언된 변수
// void study() { int score = 100; }