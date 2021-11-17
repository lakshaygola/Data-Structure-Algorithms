/* For the given tree we have to find out the shortest distance between the given two nodes 
Distance -- Number of edges required to traverse in order to reach the node */

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

// Function to calculate the distanct between the root and the node
int getDist(node* root,  int n1, int dist){
    if(root == NULL)
        return -1;
    if (root -> data == n1)
        return dist;

    int left = getDist(root->left, n1, dist+1);

    if (left != -1)
        return left;

    return getDist(root -> right, n1, dist+1);
}

// Function to find the shortest distance between nodes
int shortDistance(node* root, int n1, int n2){
    node* lcs = LCS(root, n1, n2);

    int d1 = getDist(lcs, n1, 0);
    int d2= getDist(lcs, n2, 0);

    return d1 + d2;
}

int main(){
    struct node* root = new node(1);
    root -> left = new node(2);
    root -> right = new node(3);
    root -> left -> left = new node(4);
    root -> right -> left = new node(5);
    root -> right -> right = new node(6);
    root -> right -> left -> left = new node(7);

    int result = shortDistance(root, 4, 7);
    cout<<result<<endl;
    
    return 0;
}