/* For the given tree we have to find the sum of all the elements
and the total number of nodes in the tree 
for example ---  1
			  2     3
			4   5  6  7
output 1) count --- 7    2) sum --- 28 */


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

// Function to find the count the of the given tree
int countNodes(node* head){
	if (head == NULL)
		return 0;
	return countNodes(head -> left) + countNodes(head -> right) + 1;
}

// Function to find the sum of all the element of the tree
int sumNode(node* head){
	if (head == NULL)
		return 0;
	return sumNode(head -> left) + sumNode(head -> right) + head -> data; 
}

int main(){

	node* head = new node(1);
	head -> left = new node(2);
	head -> right = new node(3);
	head -> left -> left = new node(4);
	head -> left -> right = new node(5);
	head -> right -> left = new node(6);
	head -> right -> right = new node(7);

	cout<<"Total number of node in the tree: "<<countNodes(head)<<endl;
	cout<<"Sum of all the nodes: "<<sumNode(head)<<endl;

	return 0;
}