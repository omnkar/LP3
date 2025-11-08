#include <bits/stdc++.h>
using namespace std;

void solve_knapsack() {
    vector<int> val = {50, 100, 150, 200};
    vector<int> wt = {8, 16, 32, 40};
    int W = 64;
    int n = val.size();

    // dp[i][w] = maximum value for first i items and capacity w
    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= W; w++) {
            if (wt[i - 1] <= w) {
                dp[i][w] = max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]],
                    dp[i - 1][w]
                );
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    cout << dp[n][W] << endl;  // Maximum total value
}

int main() {
    solve_knapsack();
    return 0;
}
