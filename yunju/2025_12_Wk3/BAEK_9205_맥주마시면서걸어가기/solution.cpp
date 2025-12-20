#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

int T;
int n;

int cal_dist(pair<int, int> a, pair<int, int> b) {
    return abs(a.first-b.first) + abs(a.second-b.second);
}

void solve() {
    cin >> n;
    pair<int, int> home;
    cin >> home.first >> home.second;

    // 사이즈 n 짜리
    // 편의점들의 좌표가 담긴 vector
    vector<pair<int, int>> conv(n);

    for (int i=0; i<n; i++) {
        cin >> conv[i].first >> conv[i].second;
    }

    pair<int, int> festival;
    cin >> festival.first >> festival.second;

    vector<bool> visited(n, false);

    queue<pair<int, int>> q;
    q.push(home);

    while (!q.empty()) {
        pair<int, int> curr = q.front();
        q.pop();

        if (cal_dist(curr, festival) <= 1000) {
            cout << "happy" << endl;
            return;
            
        } 
        for (int i=0; i<n; i++) {
            if (!visited[i] && cal_dist(curr, conv[i]) <= 1000) {
                visited[i] = true;
                q.push(conv[i]);
            }
        }
    }
    cout << "sad" << endl;
    
}
int main() {
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}