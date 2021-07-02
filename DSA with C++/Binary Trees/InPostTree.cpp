/* Given two arrays representing the inorder and the postorder of 
the tree we have to make the tree using that inorder and the post
order */

#include "bits/stdc++.h"

using namespace std;

// Structure of the node used in the tree
struct node{
	int data;
	struct node* left;
	struct node* right;

	node (int val){
		data = val;
		left = NULL;
		right = NULL;
	}
	
};


// Helper function serach to search the element in the inorder
int search(int inorder[], int val, int start, int end){

	for (int i = start; i <= end; i++){
		if (inorder[i] == val)
			return i;
	}
	return -1;
}

// Function to make the tree (using inorder and preorder)
node* InPreTree(int inorder[], int preorder[], int start, int end){
	int idx = 0, current, pos;

	if (start > end)
		return NULL;

	current = preorder[idx];
	idx++;
	node* temp = new node(current);

	if (start == end){
		return temp;
	}

	pos = search(inorder, current, start, end);
	temp -> left = InPreTree(inorder, preorder, start, pos-1);
	temp -> right = InPreTree(inorder, preorder, pos+1, end);

	return temp;
}

// Function to make the tree (using inorder and postorder)
node* InPostTree(int inorder[], int postorder[], int start, int end){
	int idx = 4, current, pos;

	if (start > end)
		return NULL;

	current = postorder[idx];
	idx--;
	node* temp = new node(current);

	if (start == end){
		return temp;
	}

	pos = search(inorder, current, start, end);
	temp -> left = InPreTree(inorder, postorder, pos+1, end);
	temp -> right = InPreTree(inorder, postorder, start, pos-1);

	return temp;
}

// Function to print the inorder of the currrent tree
void printInorder(node* head){
	if (head == NULL){
		return;
	}
	printInorder(head -> left);
	cout<<head -> data<<" ";
	printInorder(head -> right);
}

int main(){

	int n;
	cin>>n;
	int inorder[n] = {3,2,1,5,4};
	int preorder[n] = {1,2,3,4,5};

	node* head = InPreTree(inorder, preorder, 0, n-1);

	printInorder(head);

	return 0;
}