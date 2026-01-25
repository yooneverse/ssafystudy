#include <iostream>
#include <string>
#include <stack>

using namespace std;
// < 나오면 > 나올때까지 그대로 출력
// 공백 기준으로 문자 뒤집기
// 부분적으로 쌓고 출력
// stack 사용
// push() / pop() 반환없이 삭제 / top() 삭제없이 반/ empty() / size()
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string S;
    // 공백 포함 한 줄 전체 읽기
    getline(cin, S);
    // 끝까지 출력할 수 있도록 줄 바꾸기 추
    S += '\n';
    
    // 스택 사용
    // <가 나오면 쌓아뒀다가 
    // 일정 부분만큼 쌓아뒀다가 출력
    stack<char> st;

    // 태그 안인지 여부
    bool is_tag = false;
    
    for (char ch : S) {
        // 태그 < 가 나오면 이전까지 스택에 있는 것들 출력
        if (ch == '<') {
            while (!st.empty()) {
                cout << st.top();  // 맨 위부터 출력
                st.pop();  // 삭제
            }
            is_tag = true;
            cout << ch;
        }
        // 태그 끝 > 가 나온다면.
        else if (ch == '>') {
            is_tag = false;
            cout << ch;
        }
        // 태그 안이라면 그대로 출력
        else if (is_tag) {
            cout << ch;
        }
        // 태그 밖
        // 공백이나 줄바꿈 시 현재 스택에 있는 문자 뒤에서부터 출력
        else {
            if (ch == ' ' || ch == '\n') {
                while (!st.empty()) {
                    cout << st.top();
                    st.pop();
                }
                if (ch == ' ') {
                    cout << ch;
                }
            }
            // 스택에 넣어줌
            else {
                st.push(ch);
            }        
        }
    }
    return 0;
}