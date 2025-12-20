#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> coins;

    int coin;
    
    for (int i=0; i<n; i++) {
        cin >> coin;
        if (coin <= k) coins.push_back(coin);    
    }

    vector<int> dp(k+1, 10001);
    dp[0] = 0;

    for (int c: coins) {
        for (int v=c; v<=k; v++) {
            dp[v] = min(dp[v], dp[v-c]+1);
        }
    }
    if (dp[k]==10001) cout << -1;
    else cout << dp[k];
    return 0;
}