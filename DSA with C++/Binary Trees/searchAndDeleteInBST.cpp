/* In the given tree write the function to perform insertion and deletion from the tree */

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

// Function to search the element in the BST
node* searchInBST(node* root, int key){
    if (root == NULL){
        return NULL;
    }
    if (root->data == key)
        return root;
    
    if (key < root->data)
        return searchInBST(root->left, key);
    
    return searchInBST(root->right, key);
}

// Function to perform deletion from the BST
node* deleteInBST(node* root, int key){
    // case1 -- deleting the leaf node

}

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
    cout<<endl;

    node* result = searchInBST(root, 50);
    if (result){
        cout<<result->data<<endl;
    }else{
        cout<<"Element is not found"<<endl;
    }
    
    return 0;
}