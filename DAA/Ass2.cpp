#include <bits/stdc++.h>
using namespace std;

// Node structure for Huffman Tree
struct Node {
    int freq;           // Frequency of symbol
    string symbol;      // Character or combined symbol
    Node* left;         // Left child
    Node* right;        // Right child
    string huff;        // '0' or '1' for tree direction

    Node(int f, string s, Node* l = nullptr, Node* r = nullptr)
        : freq(f), symbol(s), left(l), right(r), huff("") {}
};

// Comparator for priority queue (min-heap)
struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq; // smaller freq -> higher priority
    }
};

// Recursive function to print Huffman codes
void printNodes(Node* root, string val = "") {
    string newVal = val + root->huff;

    if (root->left)
        printNodes(root->left, newVal);
    if (root->right)
        printNodes(root->right, newVal);

    // Leaf node
    if (!root->left && !root->right)
        cout << root->symbol << " -> " << newVal << "\n";
}

int main() {
    vector<char> chars = {'a', 'b', 'c', 'd', 'e', 'f'};
    vector<int> freq = {5, 9, 12, 13, 16, 45};

    priority_queue<Node*, vector<Node*>, Compare> pq;

    // Create leaf nodes for each character
    for (int i = 0; i < chars.size(); i++) {
        pq.push(new Node(freq[i], string(1, chars[i])));
    }

    // Build Huffman Tree
    while (pq.size() > 1) {
        Node* left = pq.top(); pq.pop();
        Node* right = pq.top(); pq.pop();

        left->huff = "0";
        right->huff = "1";

        Node* newNode = new Node(left->freq + right->freq, left->symbol + right->symbol, left, right);
        pq.push(newNode);
    }

    // Print Huffman Codes
    Node* root = pq.top();
    printNodes(root);

    return 0;
}
