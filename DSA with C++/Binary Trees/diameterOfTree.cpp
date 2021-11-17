/* Function to calculate the diameter of the tree -- diameter is the distance between two leaves 
node */
#include "bits/stdc++.h"

using namespace std;

// class to define the structure of the tree
struct node {
	int data;
	node* left;
	node* right;

	node (int val){
		data = val;
		left = NULL;
		right = NULL;
	}
};

// Function to calculate the height of the tree
int calHeight(node* head){
	if (head == NULL)
		return 0;
	int leftTree =  calHeight(head -> left);
	int rightTree = calHeight(head -> right);
	if (rightTree > leftTree) {return rightTree + 1;}
	else {return leftTree + 1;}
}

// Function to calculate the diameter
int diameterOfTree(node* root){
    if(root == NULL)
        return 0;

    int leftHt = calHeight(root -> left);
    int rightHt = calHeight(root -> right);
    int currDia = leftHt + rightHt + 1;

    int leftDia = diameterOfTree(root -> left);
    int rightDia = diameterOfTree(root -> right);

    return max(currDia, max(leftDia, rightDia));
}

int main(){
    node* head = new node(1);
	head -> left = new node(2);
	head -> right = new node(3);
	head -> left -> left = new node(4);
	head -> left -> right = new node(5);
	head -> right -> left = new node(6);
	head -> right -> right = new node(7);

	cout<<"Diameter of the tree: "<<diameterOfTree(head)<<"\n";

	return 0;
}