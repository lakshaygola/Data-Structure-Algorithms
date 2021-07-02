/* Tree is given we have to find the sum of all the element in k 
level. For example -- for the given tree
                 1
			  2     3
			4   5  6  7

output -- for k = 2 --- 4+5+6+7 = 22 */

# include "bits/stdc++.h"

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

// Function to find the sum of the k level element 
int kLevelSum(node* head, int k){

	if (head == NULL){
		return -1;
	}

	int level = 0, sum = 0; 
	queue <node*> q;
	q.push(head);
	q.push(NULL);

	while (!q.empty()){
		if (level == k)
			break;
		node* current = q.front();
		q.pop();
		if (current != NULL){
			if (current -> left != NULL)
				q.push(current -> left);

			if (current -> right != NULL)
				q.push(current -> right);
		}
		
		else if (!q.empty()){
			level++;
			q.push(NULL);
		}

	}

	while (!q.empty()){
		node* val = q.front();
		q.pop();
		if (val != NULL)
			sum += val ->data;
	}

	return sum;
}

int main(){

	int k;
	cin>>k;

	node* head = new node(1);
	head -> left = new node(2);
	head -> right = new node(3);
	head -> left -> left = new node(4);
	head -> left -> right = new node(5);
	head -> right -> left = new node(6);
	head -> right -> right = new node(7);

	int result = kLevelSum(head, k);
	cout<<"sum of the "<<k<<" level is: "<<result<<endl;

	return 0;
}