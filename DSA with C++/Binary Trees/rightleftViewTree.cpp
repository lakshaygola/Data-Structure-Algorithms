/* Write a function to print all the nodes which are visible from the left side and the right side 
of the view */
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

// Function to print the right side of the tree
void rightView(node* root){
    if (root == NULL){
        return;
    }
    queue<node*> q;
    q.push(root);
    while (!q.empty()){
        int n = q.size();
        for (int i = 0; i<n; i++){
            node* temp = q.front();
            q.pop();
            if (i == n-1){
                cout<< temp -> data<<" ";
            }
            if (temp -> left != NULL){
                q.push(temp -> left);
            }
            if (temp -> right != NULL){
                q.push(temp -> right);
            }
        }
    }
}

// Function to print the left side of the tree
void leftView(node* root){
    if (root == NULL){
        return;
    }
    queue<node*> q;
    q.push(root);
    while (!q.empty()){
        int n = q.size();
        for (int i = 0; i<n; i++){
            node* temp = q.front();
            q.pop();
            if (i == 0){
                cout<< temp -> data<<" ";
            }
            if (temp -> left != NULL){
                q.push(temp -> left);
            }
            if (temp -> right != NULL){
                q.push(temp -> right);
            }
        }
    }
}

int main(){
    struct node* root = new node(1);
    root -> left = new node(2);
    root -> right = new node(3);
    root -> left -> left = new node(4);
    root -> left -> right = new node(5);

    cout<<"Right side view: ";
    rightView(root);
    cout<<endl;
    cout<<"Left side view: ";
    leftView(root);

    return 0;
}