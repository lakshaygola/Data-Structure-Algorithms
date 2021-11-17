/* Inorder, Postorder, PreOrder traversal of the tree */

#include "bits/stdc++.h"

using namespace std;

// Structure of the tree
struct node
{
    int data;
    node* left;
    node* right;

    node(int val){
        data = val;
        left = NULL;
        right = NULL;
    }
};

// Function to print the preorder travesral of the tree
void preorder(struct node* root){
    if (root == NULL)
        return;
    cout<<root -> data<<" ";
    preorder(root -> left);
    preorder(root -> right);
}

// Function to print the inorder traversal of the tree
void inorder(struct node* root){
    if (root == NULL)
        return;
    inorder(root -> left);
    cout<<root -> data<<" ";
    inorder(root -> right);
}

// Function to print the postorder traversal of the tree
void postorder(struct node* root){
    if (root == NULL)
        return;
    postorder(root -> left);
    postorder(root -> right);
    cout<<root -> data<<" ";
}

int main(){

    /*     1
          / \
         2   3
        / \
       4   5 */

    struct node* root = new node(1);
    root -> left = new node(2);
    root -> right = new node(3);
    root -> left -> left = new node(4);
    root -> left -> right = new node(5);

    cout<<"preorder: ";
    preorder(root);
    cout<<"inorder: ";
    inorder(root);
    cout<<"postorder: ";
    postorder(root);

    return 0;
}