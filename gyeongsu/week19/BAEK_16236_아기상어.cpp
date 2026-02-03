#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <tuple>
using namespace std;

vector<pair<int, int>> directions = {{-1,0}, {0,-1}, {0,1}, {1,0}};
vector<vector<int>> Map;

tuple<int, int, int> bfs(int sr, int sc, int size, int n) {
    deque<tuple<int, int, int>> q; // r, c, cost
    q.push_back({sr, sc, 0});
    
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    visited[sr][sc] = true;
    
    int min_cost = n*n + 1;
    vector<pair<int, int>> candidate;
    
    while (!q.empty()) {
        auto [r, c, cost] = q.front();
        q.pop_front();
        
        if (cost >= min_cost) {
            sort(candidate.begin(), candidate.end());
            return {candidate[0].first, candidate[0].second, min_cost};
        }
        
        for (auto [dr, dc] : directions) {
            int nr = r + dr, nc = c + dc;
            
            if (0 <= nr && nr < n && 0 <= nc && nc < n && !visited[nr][nc]) {
                if (Map[nr][nc] > size) {
                    continue;
                }
                
                
                if (0 < Map[nr][nc] && Map[nr][nc] < size){
                    min_cost = cost +1;
                    candidate.push_back({nr, nc});
                }
                
                visited[nr][nc] = true;
                q.push_back({nr, nc, cost + 1});
            }
        }
    }
    return {-1, -1, -1};
}



int main(){
    int n;
    cin >> n;
    
    int sr, sc;
    Map.resize(n, vector<int>(n));
    
    for (int i=0; i <n; i++){
        for (int j=0; j <n; j++){
            cin >> Map[i][j];
            if (Map[i][j] == 9){
            sr = i;
            sc = j;
            Map[i][j] = 0;
            }
        }
    }
    
    int Exp = 0;
    int size = 2;
    int ans = 0;
    
    while (true){
        auto [nr, nc, dist] = bfs(sr, sc, size, n);
        
        if (dist == -1){
            break;
        }
        
        ans += dist;
        Exp ++;
        Map[nr][nc] = 0;
        sr = nr, sc = nc;
        
        if (Exp == size){
            size ++;
            Exp = 0;
        }
    }
    
    cout << ans << endl;
    return 0;
    
}
