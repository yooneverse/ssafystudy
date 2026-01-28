#include <iostream>
#include <string>
#include <vector>
using namespace std;

// 나이가 가장 적은 사람과 가장 많은 사람을 출력
// 방법1. oldest, eldest 지정 후 최신화
// 각각 처리하기 귀찮음
// !!주의점: 년도를 명확하게 처
// 생년월일이 숫자가 작을수록 연장자
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    string person;
    string e_person;
    string o_person;

    int day, month, year;
    int e_day, e_month, e_year;
    int o_day, o_month, o_year;
    
    // 첫 사람을 기준으로 설정
    cin >> person >> day >> month >> year;
    o_person = e_person = person;
    e_day = o_day = day;
    e_month = o_month = month;
    e_year = o_year = year;

    // 이후 사람들로 최신화
    for (int i=1; i<n; i++) {
        cin >> person >> day >> month >> year;

        // 나이 많은 사람 최신화
        if (year < o_year) { 
            o_person = person;
            o_year = year;
            o_month = month;
            o_day = day;
        } else if (year == o_year) {
            if (month < o_month) {
                o_person = person; o_year = year; o_month = month; o_day = day;
            }
            else if (month == o_month) {
                if (day < o_day) {
                    o_person = person; o_year = year; o_month = month; o_day = day;
                }
            }
        }
        // 나이 어린 사람 최신화
        if (year > e_year) {
            e_person = person;
            e_year = year;
            e_month = month;
            e_day = day;
        } else if (year == e_year) {
            if (month > e_month) {
                e_person = person; e_year = year; e_month = month; e_day = day;
            }
            else if (month == e_month) {
                if (day > e_day) {
                    e_person = person; e_year = year; e_month = month; e_day = day;
                }
            }
        }
    }

    cout << e_person << "\n" << o_person;

    
    return 0;
}