/* Function to perform insertion in BST */

#include "bits/stdc++.h"

using namespace std;

// Structure of the BST
struct node {
    int data;
    node* right, *left;

    node(int val){
        data = val;
        left = NULL;
        right = NULL;
    }
};

// Function to perform the insertion in the tree
node* insertion(node* root, int val){
    if (root == NULL){
        return new node(val);
    }
    if (val < root->data)
        root->left = insertion(root->left, val);
    if (val > root->data)
        root->right = insertion(root->right, val);

    return root;
}

// Function to print the inorder of the tree
void inorder(node* root){
    if (root == NULL)
        return;
    inorder(root->left);
    cout<<root->data<<" ";
    inorder(root->right);
}

int main(){
    node* root = NULL;
    root = insertion(root, 5);
    insertion(root, 2);
    insertion(root, 8);
    insertion(root, 1);
    insertion(root, 12);
    insertion(root, 4);

    inorder(root);
    
    return 0;
}