#include <bits/stdc++.h>
using namespace std;

struct Item {
    int value, weight;
    Item(int v, int w) : value(v), weight(w) {}
};

// -------------------- DYNAMIC PROGRAMMING --------------------
int knapsackDP(vector<Item> &items, int W) {
    int n = items.size();
    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= W; w++) {
            if (items[i - 1].weight <= w)
                dp[i][w] = max(items[i - 1].value + dp[i - 1][w - items[i - 1].weight],
                               dp[i - 1][w]);
            else
                dp[i][w] = dp[i - 1][w];
        }
    }

    cout << "\nDP Table:\n";
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++)
            cout << setw(4) << dp[i][w];
        cout << endl;
    }

    return dp[n][W]; // Final answer
}

// -------------------- BRANCH AND BOUND --------------------
struct Node {
    int level, profit, bound, weight;
};

bool cmp(Item a, Item b) {
    double r1 = (double)a.value / a.weight;
    double r2 = (double)b.value / b.weight;
    return r1 > r2; // sort by decreasing value/weight ratio
}

// function to calculate upper bound on profit
int bound(Node u, int n, int W, vector<Item> &arr) {
    if (u.weight >= W) return 0;

    int profit_bound = u.profit;
    int j = u.level + 1;
    int totweight = u.weight;

    while ((j < n) && (totweight + arr[j].weight <= W)) {
        totweight += arr[j].weight;
        profit_bound += arr[j].value;
        j++;
    }

    if (j < n)
        profit_bound += (W - totweight) * arr[j].value / arr[j].weight;

    return profit_bound;
}

int knapsackBnB(vector<Item> &arr, int W) {
    sort(arr.begin(), arr.end(), cmp);
    queue<Node> Q;
    Node u, v;
    int n = arr.size();
    u.level = -1;
    u.profit = u.weight = 0;
    int maxProfit = 0;
    Q.push(u);

    while (!Q.empty()) {
        u = Q.front();
        Q.pop();

        if (u.level == n - 1) continue;
        v.level = u.level + 1;

        // 1. Take item
        v.weight = u.weight + arr[v.level].weight;
        v.profit = u.profit + arr[v.level].value;

        if (v.weight <= W && v.profit > maxProfit)
            maxProfit = v.profit;

        v.bound = bound(v, n, W, arr);
        if (v.bound > maxProfit)
            Q.push(v);

        // 2. Skip item
        v.weight = u.weight;
        v.profit = u.profit;
        v.bound = bound(v, n, W, arr);
        if (v.bound > maxProfit)
            Q.push(v);
    }

    return maxProfit;
}

// -------------------- MAIN FUNCTION --------------------
int main() {
    vector<Item> items = {
        {50, 8}, {100, 16}, {150, 32}, {200, 40}
    };
    int W = 64;
    int choice;

    cout << "0/1 Knapsack Problem\n";
    cout << "----------------------\n";
    cout << "1. Dynamic Programming\n";
    cout << "2. Branch and Bound\n";
    cout << "Enter your choice: ";
    cin >> choice;

    switch (choice) {
    case 1: {
        int maxVal = knapsackDP(items, W);
        cout << "\nMaximum Value (DP): " << maxVal << endl;
        break;
    }
    case 2: {
        int maxVal = knapsackBnB(items, W);
        cout << "\nMaximum Value (Branch & Bound): " << maxVal << endl;
        break;
    }
    default:
        cout << "Invalid choice!" << endl;
    }

    return 0;
}
