#include <bits/stdc++.h>
using namespace std;

int n;
int start_row, start_col;
vector<vector<string>> res;

void backtrack(int r, vector<string>& board,
               unordered_set<int>& col,
               unordered_set<int>& posDiag,
               unordered_set<int>& negDiag) {
    if (r == n) {
        res.push_back(board);
        return;
    }

    // Skip the fixed starting queen row
    if (r == start_row) {
        backtrack(r + 1, board, col, posDiag, negDiag);
        return;
    }

    for (int c = 0; c < n; c++) {
        if (col.count(c) || posDiag.count(r + c) || negDiag.count(r - c))
            continue;

        // Choose
        col.insert(c);
        posDiag.insert(r + c);
        negDiag.insert(r - c);
        board[r][c] = '1';

        // Explore
        backtrack(r + 1, board, col, posDiag, negDiag);

        // Undo choice
        col.erase(c);
        posDiag.erase(r + c);
        negDiag.erase(r - c);
        board[r][c] = '0';
    }
}

void n_queens(int n_input, int s_row, int s_col) {
    n = n_input;
    start_row = s_row;
    start_col = s_col;

    unordered_set<int> col, posDiag, negDiag;
    vector<string> board(n, string(n, '0'));

    // Place the fixed queen
    col.insert(start_col);
    posDiag.insert(start_row + start_col);
    negDiag.insert(start_row - start_col);
    board[start_row][start_col] = '1';

    backtrack(0, board, col, posDiag, negDiag);

    // Print all valid solutions
    for (auto& sol : res) {
        for (auto& row : sol)
            cout << row << "\n";
        cout << "\n";
    }
}

int main() {
    int n = 8;
    int start_row = 0, start_col = 0;
    n_queens(n, start_row, start_col);
    return 0;
}
