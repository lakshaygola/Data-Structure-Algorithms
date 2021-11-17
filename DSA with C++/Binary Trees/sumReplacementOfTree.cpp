/* Replace all the node of the tree with the sum of left and right subtree and of itself */

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

// Function to replace node value with the sum of the left and right subtree and itself
void sumReplace(node* &root){
    if (root == NULL)
        return;
    sumReplace(root -> left);
    sumReplace(root -> right);

    if (root->left != NULL){
        root->data += root->left->data;
    }
    if (root->right != NULL){
        root->data += root->right->data;
    }
} 

// Function to print the preorder of the tree
void preorder(struct node* root){
    if (root == NULL)
        return;
    cout<<root -> data<<" ";
    preorder(root -> left);
    preorder(root -> right);
}

int main(){
    struct node* root = new node(1);
    root -> left = new node(2);
    root -> right = new node(3);
    root -> left -> left = new node(4);
    root -> left -> right = new node(5);
    preorder(root);
    cout<<"\n";
    sumReplace(root);
    preorder(root);
    
    return 0;
}