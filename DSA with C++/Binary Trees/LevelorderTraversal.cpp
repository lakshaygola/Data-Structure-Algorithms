/* We have a tree and we have to traverse it level wise means 
first we print the level 0 elements of the tree then level 1 and so 
on
for example ---  1
			  2     3
			4   5  6  7
output for this tree ---  1-2-3-4-5-6-7 */

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


// Function to print the in order traversal
void inorder(node* head){
	if (head == NULL){
		return;
	}

	inorder(head -> left);
	cout<<head -> data<<" ";
	inorder(head -> right);
}

// Function to traverse the tree in level order
void levelOrderTraversal(node* head){

	if (head == NULL){
		return;
	}

	queue <node*> elements;
	elements.push(head);
	elements.push(NULL);

	while (!elements.empty()){
		node* current = elements.front();
		elements.pop();
		if (current != NULL){
			cout<<current -> data<<" ";

			if (current -> left != NULL)
				elements.push(current -> left);

			if (current -> right != NULL)
				elements.push(current -> right);
		} 
		else if (!elements.empty()){
			elements.push(NULL);
		}
	}
}

int main(){

	node* head = new node(1);
	head -> left = new node(2);
	head -> right = new node(3);
	head -> left -> left = new node(4);
	head -> left -> right = new node(5);
	head -> right -> left = new node(6);
	head -> right -> right = new node(7);

	cout<<"Print the Indorder traversal of the tree: ";
	inorder(head);

	cout<<"\nLevel traversal: ";
	levelOrderTraversal(head);

	return 0;
}