#include <bits/stdc++.h>
using namespace std;

long long comparisons = 0;

// ------------------ Deterministic Quick Sort ------------------
vector<int> deterministic_quick_sort(vector<int> arr) {
    if (arr.size() <= 1)
        return arr;

    int pivot = arr[0];
    vector<int> left, right;

    for (size_t i = 1; i < arr.size(); i++) {
        comparisons++;
        if (arr[i] < pivot)
            left.push_back(arr[i]);
        else
            right.push_back(arr[i]);
    }

    vector<int> sorted_left = deterministic_quick_sort(left);
    vector<int> sorted_right = deterministic_quick_sort(right);

    sorted_left.push_back(pivot);
    sorted_left.insert(sorted_left.end(), sorted_right.begin(), sorted_right.end());
    return sorted_left;
}

// ------------------ Randomized Quick Sort ------------------
vector<int> randomized_quick_sort(vector<int> arr) {
    if (arr.size() <= 1)
        return arr;

    int pivot_idx = rand() % arr.size();
    int pivot = arr[pivot_idx];
    vector<int> left, right;

    for (size_t i = 0; i < arr.size(); i++) {
        if (i == pivot_idx) continue;
        comparisons++;
        if (arr[i] < pivot)
            left.push_back(arr[i]);
        else
            right.push_back(arr[i]);
    }

    vector<int> sorted_left = randomized_quick_sort(left);
    vector<int> sorted_right = randomized_quick_sort(right);

    sorted_left.push_back(pivot);
    sorted_left.insert(sorted_left.end(), sorted_right.begin(), sorted_right.end());
    return sorted_left;
}

// ------------------ Comparison Counter ------------------
pair<long long, vector<int>> count_comparisons(vector<int> arr,
                                               vector<int> (*sorting_algorithm)(vector<int>)) {
    comparisons = 0;
    vector<int> sorted_arr = sorting_algorithm(arr);
    return {comparisons, sorted_arr};
}

// ------------------ Main Function ------------------
int main() {
    srand(time(0));

    vector<int> input_list = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5};

    auto [deterministic_comparisons, deterministic_sorted] =
        count_comparisons(input_list, deterministic_quick_sort);

    cout << "Deterministic Quick Sort:\n";
    cout << "Comparisons: " << deterministic_comparisons << "\n";
    cout << "Sorted Array: ";
    for (int x : deterministic_sorted) cout << x << " ";
    cout << "\n\n";

    auto [randomized_comparisons, randomized_sorted] =
        count_comparisons(input_list, randomized_quick_sort);

    cout << "Randomized Quick Sort:\n";
    cout << "Comparisons: " << randomized_comparisons << "\n";
    cout << "Sorted Array: ";
    for (int x : randomized_sorted) cout << x << " ";
    cout << "\n";

    return 0;
}
