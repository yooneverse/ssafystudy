#include <iostream>
#include <string>

using namespace std;

// 나이가 가장 적은 사람과 가장 많은 사람을 출력
// 방법2. 나이를 하나의 정수로 처리
// 변수명 깔끔하게
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    string max_person, min_person;

    // 기준 나이 초기 설정
    int min_val = 21000000;
    int max_val = 0;

    for (int i=0; i<n; i++) {
        string name;
        int d, m, y;
        cin >> name >> d >> m >> y;

        // 20001020 와 같이 변환
        int birth = y*10000 + m*100 + d;

        if (birth < min_val) {
            min_val = birth;
            min_person = name; 
        }

        if (birth > max_val) {
            max_val = birth;
            max_person = name; 
        }
    }
    
    cout << max_person << "\n" << min_person;

    return 0;
}