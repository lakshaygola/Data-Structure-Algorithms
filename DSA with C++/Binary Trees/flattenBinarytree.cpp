/* We have to flatten out the given binary tree -- such that each node have NULL as a left child */

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

// Function to flatten out the binary tree
void flattentree(node* &root){
    if (root == NULL or (root -> left == NULL and root -> right == NULL))
        return;
    if (root -> left != NULL){
        flattentree(root -> left);
        node* temp = root -> right;
        root -> right = root -> left;
        root -> left = NULL;
        node* t = root -> right;
        while (t -> right != NULL){
            t =  t->right;
        }t->right = temp;
    }
    flattentree(root -> right);
}

// Function to print the pre order of the tree
void preorder(node* root){
    if (root == NULL)
        return;
    cout<<root->data<<" ";
    preorder(root->left);
    preorder(root->right); 
}

int main(){
    struct node* root = new node(1);
    root -> left = new node(2);
    root -> right = new node(3);
    root -> left -> left = new node(4);
    root -> left -> right = new node(5);
    cout<<"before"<<endl;
    preorder(root);
    flattentree(root);
    cout<<"after"<<endl;
    preorder(root);
    return 0;
}