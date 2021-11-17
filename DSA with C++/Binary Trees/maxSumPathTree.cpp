/* For the given tree we have to find the path which have maximum sum */

#include "bits/stdc++.h"

using namespace std;

struct node{
    int data;
    node* left;
    node* right;

    node(int val){
        data = val;
        left = right = NULL;
    }
};

// Helper Function
int maxSum(node* root, int &sum){
    if (root == NULL){
        return 0;
    }
    int lt = maxSum(root -> left, sum);
    int rt = maxSum(root -> right, sum);
    int nodeSum = max(max(root->data, root->data + lt + rt), max(lt + root->data, rt + root->data));

    sum = max(sum, nodeSum);

    int singlePathSum = max(root -> data, max(root -> data + lt, root -> data + rt));
    return singlePathSum;
}

// Main function
int maxSumPath(node* root){
    int ans = INT_MIN;
    maxSum(root, ans);
    return ans;
}

int main(){
    struct node* root = new node(1);
    root -> left = new node(2);
    root -> right = new node(3);
    root -> left -> left = new node(4);
    root -> right -> left = new node(5);
    root -> right -> right = new node(6);
    root -> right -> left -> left = new node(7);

    int ans = maxSumPath(root);
    cout<<ans<<"\n";

    return 0;
}