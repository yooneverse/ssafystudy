#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e16;

struct Edge {
    int to;
    int weight;
};

struct State {
    long long cost;
    int node;
    int step; 

    bool operator>(const State& other) const {
        return cost > other.cost;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<long long> dist_fox(n + 1, INF);
    dist_fox[1] = 0;
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq_fox;
    pq_fox.push({0, 1});

    while (!pq_fox.empty()) {
        long long d = pq_fox.top().first;
        int u = pq_fox.top().second;
        pq_fox.pop();

        if (dist_fox[u] < d) continue;

        for (auto& edge : adj[u]) {
            long long next_d = d + edge.weight * 2;
            if (next_d < dist_fox[edge.to]) {
                dist_fox[edge.to] = next_d;
                pq_fox.push({next_d, edge.to});
            }
        }
    }

    vector<vector<long long>> dist_wolf(n + 1, vector<long long>(2, INF));
    dist_wolf[1][0] = 0;
    priority_queue<State, vector<State>, greater<State>> pq_wolf;
    pq_wolf.push({0, 1, 0});

    while (!pq_wolf.empty()) {
        long long d = pq_wolf.top().cost;
        int u = pq_wolf.top().node;
        int s = pq_wolf.top().step;
        pq_wolf.pop();

        if (dist_wolf[u][s] < d) continue;

        
        
        for (auto& edge : adj[u]) {
            int next_s = 1 - s;
            long long weight = (s == 0) ? edge.weight : (long long)edge.weight * 4;
            long long next_d = d + weight;

            if (next_d < dist_wolf[edge.to][next_s]) {
                dist_wolf[edge.to][next_s] = next_d;
                pq_wolf.push({next_d, edge.to, next_s});
            }
        }
    }

    int ans = 0;
    for (int i = 2; i <= n; i++) {
        long long wolf_min = min(dist_wolf[i][0], dist_wolf[i][1]);
        if (dist_fox[i] < wolf_min) {
            ans++;
        }
    }

    
    cout << ans;

    return 0;
}