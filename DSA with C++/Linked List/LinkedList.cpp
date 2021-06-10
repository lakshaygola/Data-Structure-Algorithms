/* Linked list and its basic operation */

#include "bits/stdc++.h"

using namespace std;

// Class node to define the basic structure of the nodes
class Node{
public: 
	int data;
	Node *next;

	Node(int val){
		data = val;
		next = NULL;
	}
};

// Function to inerst the node at the tail / end
void insertAtTail(Node* &head, int val){
	Node* temp = new Node(val);

    if (head == NULL){
        head = temp;
        return;
    }

    Node* p = head;
    while (p->next != NULL){
        p = p->next;
    }
	p->next= temp;
}

// Function to add the element to the head of the list
void insertAthead(Node* &head, int val){
    Node *temp= new Node(val);

    temp->next = head;
    head = temp;
}

// Function to print all the linked list
void print(Node *head){
    Node *p= head;
    while (p != NULL){
        cout<<p->data<<" ";
        p= p->next;
    }
    cout<<endl;
}

int main(){

    Node *head= NULL;

    insertAtTail(head, 50);
    insertAtTail(head, 82);
    insertAtTail(head, 89);

    insertAthead(head, 60);
    print(head);

	return 0;
}