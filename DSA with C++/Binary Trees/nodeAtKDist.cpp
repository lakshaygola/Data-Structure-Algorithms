/* For the given node in the tree print all the nodes which is at k distance with the target node */

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

// Function to print the k nodes in the same subtree
void subtreeKDist(node* root, int k){
    if (root == NULL || k < 0){
        return;
    }
    if (k == 0){
        cout<<root -> data<<" ";
    }
    subtreeKDist(root -> left, k-1);
    subtreeKDist(root -> right, k-1);
    return;
}

// Function to print the nodes at k distance
int Kdist(node* root, node* target, int k){
    if (root == NULL){
        return -1;
    }
    if (root == target){
        subtreeKDist(root, k);
        return 0;
    }

    int dl = Kdist(root -> left, target, k);
    if (dl != -1){
        if (dl + 1 == k){
            cout<<root -> data<<" ";
        }else{
            subtreeKDist(root -> right, k - dl - 2);
        }
        return 1 + dl;
    }

    int dr = Kdist(root -> right, target, k);
    if (dr != -1){
        if (dr + 1 == k){
            cout<<root -> data<<" ";
        }else{
            subtreeKDist(root -> left, k - dr - 2);
        }
        return 1 + dr;
    }
    return -1;
}

int main(){
    struct node* root = new node(1);
    root -> left = new node(2);
    root -> right = new node(3);
    root -> left -> left = new node(4);
    root -> right -> left = new node(5);
    root -> right -> right = new node(6);
    root -> right -> left -> left = new node(7);

    node* root1 = NULL;

    int k;
    cin>>k;
    Kdist(root, root -> right, k);
    
    return 0;
}