/* For the given two nodes of the tree we have to find the lowest common ancestor for both these 
nodes */

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

// Function to find the lowest common ancestor of the given nodes
node* LCS(node* root, int n1, int n2){
    if (root == NULL){
        return NULL;
    }

    if (root -> data == n1 or root -> data == n2){
        return root;
    }

    node* left = LCS(root -> left, n1, n2);
    node* right = LCS(root -> right, n1, n2);

    if (left and right)
        return root;

    if (left != NULL){
        return left;
    }return right;
}

int main(){

    struct node* root = new node(1);
    root -> left = new node(2);
    root -> right = new node(3);
    root -> left -> left = new node(4);
    root -> right -> left = new node(5);
    root -> right -> right = new node(6);
    root -> right -> left -> left = new node(7);

    node* result = LCS(root, 6, 7);

    if (result){
        cout<<result -> data<<endl;
    }else{
        cout<<"No Common Ancestor Exist for these nodes"<<endl;
    }

    return 0;
}