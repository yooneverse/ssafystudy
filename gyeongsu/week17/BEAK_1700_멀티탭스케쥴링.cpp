/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

// 가전의 종류를 페이지로 생각각

int n, k;
vector<int> v;
map<int, deque<int>> m; // 종류, 순서
priority_queue<pair<int, int>> schedule; // n크기의 최대힙, 다음 번에 등장하는 위치, 페이지 번호
bool on_page[101]; // python set역할


int main()
{
    cin >> n >> k;
    
    int page;
    for(int i=0; i<k; i++){
        
        cin >> page;
        v.push_back(page); // 페이지 순서
        m[page].push_back(i); // 각 페이지가 등장하는 위치 저장하는 map
    }
    
    
    
    // v에 차근 차근 채운다
    // 다 차고 페이지 교체가 필요한 시점
    
    // 다음 번 등장하는 위치가 가장 멀리 있는 녀석을 교체한다.
    
    int ans =0;
    int pq_size = 0;
    for(int i=0; i<k; i++){
        // cout << "------------------------\n";
        // cout << "i-" << i << '\n';
        int now_page = v[i]; // 현재 들어가야할 페이지
        int page_ord = 1001;

        
        if (on_page[now_page]){ // 이미 활성화 된 페이지가 다시 들어오면
            
            m[now_page].pop_front(); // 페이지로 가서 이번에 들어가는 페이지를 비우고
            if(!m[now_page].empty()){
                // cout << now_page << "있음\n";
                page_ord = m[now_page].front(); // 현재 페이지의 다음 순서를 가져옴
            }
            schedule.push({page_ord, now_page}); // 스케쥴표 넣어주되, 힙사이즈는 유지지
            continue;
        } 


        if (pq_size >= n) { 
            // cout << schedule.top().second << "교체\n";
            on_page[schedule.top().second] = false;
            schedule.pop();
            pq_size--;
            
            ans++;
        }
        
        m[now_page].pop_front(); // 페이지로 가서 이번에 들어가는 페이지를 비우고
        
        if(!m[now_page].empty()){
            page_ord = m[now_page].front(); // 다음번 등장하는 페이지의 순서를 가져옴
        }
        
        schedule.push({page_ord, now_page}); // 스케쥴표 업데이트
        pq_size++; // 힙큐 사이즈 반영
        on_page[now_page] = true; // 현재 페이지 활성화       
        
        // cout << now_page << "번 페이지 삽입 다음 등장 순서 " << page_ord << "\n" << "현재 힙큐 사이즈:" << pq_size << '\n';
 
    }
    
    cout << ans;
    

    return 0;
}