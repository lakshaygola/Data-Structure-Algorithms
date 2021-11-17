/* For the given tree find out whether it is height balance or not */

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

// Function to calculate the height of the tree
int height(node* root){
    if (root == NULL)
        return 0;
    int lh = height(root -> left);
    int rh = height(root -> right);
    return max(lh, rh) + 1;
}

// Function to find the tree is balance or not
// bool isBalance(node* root){
//     if (root == NULL)
//         return true;
//     if (isBalance(root -> left) == false)
//         return false;
//     if (isBalance(root -> right) == false)
//         return false;
    
//     int leftHt = height(root -> left);
//     int rightHt = height(root -> right);
//     if (abs(leftHt - rightHt) <= 1)
//         return true;
//     else
//         return false;
// }

// Optimized function for find the balance tree
bool isBalance(node* root, int* height){
    if (root == NULL)
        return true;

    int lh = 0, rh = 0;
    if (isBalance(root -> left, &lh) == false)
        return false;
    if (isBalance(root -> right, &rh) == false)
        return false;
    
    *height = max(lh, rh) + 1;
    if (abs(lh - rh)<=1)
        return true;
    else
        return false;
}

int main(){
    struct node* root = new node(1);
    root -> left = new node(2);
    root -> right = new node(3);
    root -> left -> left = new node(4);
    root -> left -> right = new node(5);

    int height = 0;
    if (isBalance(root, &height)){
        cout<<"Tree is balance"<<"\n";
    }else{
        cout<<"Not balance"<<"\n";
    }

    return 0;
}