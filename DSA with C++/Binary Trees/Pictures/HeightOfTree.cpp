/* For the given tree we have to find the height of the tree
for example ---  1
			  2     3
			4   5  6  7
output --- height of the tree --- 3 */

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

// Function to find the height of the tree
int heigthOfTree(node* head){
	if (head == NULL)
		return 0;
	int leftTree =  heigthOfTree(head -> left);
	int rightTree = heigthOfTree(head -> right);
	if (rightTree > leftTree) {return rightTree + 1;}
	else {return leftTree + 1;}
}

int main(){
 
	node* head = new node(1);
	head -> left = new node(2);
	head -> right = new node(3);
	head -> left -> left = new node(4);
	head -> left -> right = new node(5);
	head -> right -> left = new node(6);
	head -> right -> right = new node(7);

	cout<<"Height of the tree: "<<heigthOfTree(head)<<endl;

	return 0;
}