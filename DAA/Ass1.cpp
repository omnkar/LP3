#include <iostream>
using namespace std;

void fibo_non_recursive(int n)
{
    int t1 = 0, t2 = 1, nextTerm = 0;
    cout << "Fibonacci Series: " << endl;
    for (int i = 1; i <= n; ++i)
    {
        if (i == 1)
        {
            cout << t1 << ", ";
            continue;
        }
        if (i == 2)
        {
            cout << t2 << ", ";
            continue;
        }
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
        cout << nextTerm << ", ";
    }
    cout << "\b\b " << endl; // To remove the last comma and space
}

void fibo_recursive(int n, int t1 = 0, int t2 = 1, int count = 1)
{
    if (count > n)
        return;
    if (count == 1)
    {
        cout << t1 << ", ";
        fibo_recursive(n, t1, t2, count + 1);
    }
    else if (count == 2)
    {
        cout << t2 << ", ";
        fibo_recursive(n, t1, t2, count + 1);
    }
    else
    {
        int nextTerm = t1 + t2;
        cout << nextTerm << ", ";
        fibo_recursive(n, t2, nextTerm, count + 1);
    }
}

int main()
{
    int n;
    cout << "Enter the number of terms: ";
    cin >> n;
    int choice;
    cout << "\n---------------Menu---------------\n";
    cout << "\n1. Non-Recursive\n2. Recursive\n";
    cout << "\nEnter your choice: ";
    cin >> choice;
    switch (choice)
    {
    case 1:
        fibo_non_recursive(n);
        break;
    case 2:
        cout << "Fibonacci Series: " << endl;
        fibo_recursive(n);
        cout << "\b\b " << endl; // To remove the last comma and space
        break;
    default:
        cout << "Invalid choice!" << endl;
        return 1;
    }
    cout << "\b\b " << endl; // To remove the last comma and space
    return 0;
}