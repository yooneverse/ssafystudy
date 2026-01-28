/*
마주보는 두 수 중 하나만 사용 가능함

1. 가장 아래줄
꼭짓점 4개의 블럭은 이어진 두 면이 보임
(N-2) * 4 개의 블럭은 하나의 면만 보임

2. 맨 윗줄
꼭짓점 4개의 블럭은 3개의 면만 보임(마주보지 않는)
(N-2) * 4 개의 블럭은 이어진 두 면이 보임
N*N - 4*(N-1) 개의 블럭은 한 면만 보임

3. 그 외
네 모서리에 존재하는 4 * (N-2)개의 블럭은 이어진 두 면이 보임
그 외 N*N - 4 * (N-1) 개의 블럭은 한 면만 보임

결국 블럭은 세 가지 타입으로 나눌 수 있음
1) 한 면만 보이는 블럭
6개의 수 중 최솟값 택하면 됨
2) 이어진 두 면이 보이는 블럭
가능한 두 수의 합 중 최솟값 선택(마주보는 두 면 제외)
3) 세 면이 보이는 블럭 (마주 보는 두 면 제외)
가능한 세 수의 합 중 최솟값 선
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N;
    cin >> N;

    int dice[6];
    for (int i=0; i<6; i++) {
        cin >> dice[i];
    }
    
    // 주사위 사이즈가 1X1X1 일 때
    if (N==1) {
        sort(dice, dice+6);
        int sum = 0;
        for (int i = 0; i<5; i++) {
            sum += dice[i];
        }
        cout << sum << "\n";
        return 0;
    }
    
    // 마주 보는 숫자들 중 작은 숫자들의 모임
    int min_sides[3];
    min_sides[0] = min(dice[0], dice[5]);
    min_sides[1] = min(dice[1], dice[4]);
    min_sides[2] = min(dice[2], dice[3]);

    // 정렬
    sort(min_sides, min_sides+3);

    long long min1 = min_sides[0];
    long long min2 = min_sides[0]+min_sides[1];
    long long min3 = min_sides[0]+min_sides[1]+min_sides[2];

    // LL long long으로 처리하여 터짐 방지
    long long n1 = 4LL * (N - 1) * (N - 2) + (N - 2) * (N - 2);
    long long n2 = 4LL * (N - 1) + 4LL * (N - 2);
    long long n3 = 4LL;

    long long ans = n1 * min1 + n2 * min2 + n3 * min3;

    cout << ans << "\n";
    return 0;
}