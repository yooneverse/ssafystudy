/*
세 자연수 n,x,y 가 주어짐

1부터 n까지의 자연수가 각 2개씩 있는 길이 2n짜리 랭퍼드 수열의 개수를 출력

단, x번째와 y번째 숫자가 같아야 함


예시)
3 1 4 가 주어진다면
1~3의 숫자가 각 2개씩 사용되고, 1번째와 4번째 숫자가 동일해야 함

생각해보자
1번째와 4번째 숫자가 같다는 것은 아주 중요한 조건
why?
1번째 숫자와 4번째 숫자 사이에는 2개의 숫자가 들어감
>> 1번째 숫자와 4번째 숫자는 1이 될 수 없다! 2만이 가능함!
2 _ _ 2 _ _ 까지 그려짐
2와 2 사이에는 1 1 불가능, 3 3도 불가능

가능한 경우는
2 3 1 2 1 3 뿐이다

3과 3 사이에는 3개의 숫자가 들어가야 한다
>> 3의 인덱스가 i 라면 다른 3의 인덱스는 i+4(or i-4)
*/
/*
위 예시를 통해 든 생각

x번째 수와 y번째 수는 알고 시작
둘 사이에 들어가는 숫자의 개수는 y-x-1개임 
>> x = y = y-x-1 

나머지 2n-2개의 숫자는 어떻게 배열할 수 있을까?

7 4 10
_ _ _ 5 _ _ _ _ _ 5 _ _ _ _

큰 숫자들부터 인덱스 앞에서부터 지정 
num = 7
i랑 i+num 같게, 두 인덱스에 이미 숫자가 있다면 다음으로
i+num이 2n이상이면 불가능 
*/

#include <iostream>
#include <vector>

// C++의 표준 라이브러리 모두 함수, 객체는 std 이름 공간 안에 있음
// std::vector<int> v; 라고 작성해야 함
// 아래 코드를 작성하면 vector<int> v; 만 작성하면 됨
// 단, 실무에서는 이름 충돌 위험 때문에 std까지 작성함
using namespace std;

int n,x,y;
int xth; // x,y번째에 올 숫자 (y-x-1)
int ans = 0;
vector<int> numbers; // 랭퍼드 수열 배열

void backtrack(int num) {
    // x,y번째 자리에 넣은 숫자라면 다음 숫자로 넘어감
    if (num == xth) {
        backtrack(num-1);
        return;
    }

    // 1까지 수열에 넣었다면 결과 1 증가
    if (num == 0) {
        ans++;
        return;
    }

    for (int i=1; i<=2*n; i++) {
        // num이라는 숫자를 넣을 두 번째 인덱스
        int second_idx = i+num+1;

        // 배열의 크기를 넘어버리면 불가능
        if (second_idx>2*n) {
            return;
        }

        // 이미 해당 자리에 다른 숫자가 있다면 다음 자리로
        if (numbers[i] != 0 || numbers[second_idx] != 0) {
            continue;
        }

        numbers[i] = num;
        numbers[second_idx] = num;

        backtrack(num-1);
        numbers[i] = 0;
        numbers[second_idx] = 0;
        
    }
}
int main() {
    // C++은 C언어 입출력 방식도 사용 가능함
    // false로 동기화를 끊어버림 >> 독립적 버퍼 사용하게 되어 속도 빨라짐
    // C언어의 입출력인 printf, scanf 등은 쓰면 안 됨
    ios_base::sync_with_stdio(false);

    // 기본적으로 cin과 cout은 묶여 있음
    // cin이 입력받으려 할 때마다 cout의 버퍼를 비움
    // (cout으로 "이름 입력하세요" 출력하고 cin으로 입력받는 느낌)
    // (코테에서는 필요없는 과정)
    // 둘의 연결을 끊어서 불필요한 시간을 단축
    cin.tie(NULL);
    
    cin >> n >> x >> y;

    // 랭퍼스 수열 2*n+1 사이즈 0으로 채우고 시작
    numbers.resize(2*n+1, 0);

    // x,y 번째 자리에 들어갈 수
    xth = y-x-1;

    numbers[x] = xth;
    numbers[y] = xth;

    backtrack(n);

    cout << ans << "\n";
    
    return 0;
}