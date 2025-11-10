#include <bits/stdc++.h>
using namespace std;

// Global variables
int N;

// ================= BACKTRACKING METHOD =================
bool isSafe(vector<string> &board,int row,int col)
{
    // for column
    int n=board.size();
    //col
    for(int i=0;i<n;i++)
    {
        if(board[i][col]=='Q') return false;
    }
    // row
    for(int i=0;i<n;i++)
    {
        if(board[row][i]=='Q'){
            return false;
        }
    }

    //up-left
    for(int i=row-1,j=col-1;i>=0 && j>=0; i--,j--)
    {
        if(board[i][j]=='Q') return false;
    }
    //up-right
    for(int i=row-1,j=col+1;i>=0 && j<n;i--,j++)
    {
        if(board[i][j]=='Q') return false;
    }

    //down-left
    for(int i=row+1,j=col-1;i<n && j>=0 ;i++,j--){
        if(board[i][j]=='Q'){
            return false;
        }
    }

    //down-right
    for(int i=row+1,j=col+1;i<n && j<n ; i++,j++){
        if(board[i][j]=='Q'){
            return false;
        }
    }
    return true;
    
}
void solveBacktracking(int row,vector<string> &board,int &count,int sx)
{
    if(row==N)
    {
        count++;
        for(string s: board)
        {
            cout<<s<<endl;
        }cout<<endl;
        return;
    }

    if(row==sx){
        solveBacktracking(row+1,board,count,sx);
        return;
    }

    for(int col=0;col<N;col++)
    {
        if(isSafe(board,row,col))
        {
            board[row][col]='Q';
            solveBacktracking(row+1,board,count,sx);
            board[row][col]='.';
        }
    }
}



void nQueensBacktracking() {
    vector<string> board(N, string(N, '.'));
    int count = 0;
    cout<<"Enter starting queen location : ";
    int sx,sy;
    cin>>sx>>sy;
    board[sx][sy]='Q';
    cout << "\n--- Solving using Backtracking ---\n\n";
    solveBacktracking(0, board, count,sx);
    cout << "Total Solutions: " << count << "\n";
}



// ================= MAIN MENU =================
int main() {
    int choice;

    do {
        cout << "\n==============================\n";
        cout << "      N - Queens Problem\n";
        cout << "==============================\n";
        cout << "1. Solve using Backtracking\n";
        cout << "2. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter board size N: ";
            cin >> N;
        }

        switch (choice) {
            case 1:
                nQueensBacktracking();
                break;
            case 2:
                cout << "Exiting program...\n";
                break;
            default:
                cout << "Invalid choice! Try again.\n";
        }

    } while (choice != 2);

    return 0;
}

n queen