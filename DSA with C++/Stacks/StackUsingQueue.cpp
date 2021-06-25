/* In this notebook we are going to implement the stack using queue */

# include "bits/stdc++.h"

using namespace std;

// Method 1 -- push method is costly

// Class to implement the stack using queue
class Queue{	
	int N;

	queue<int> q1;
	queue<int> q2;

public:
	Queue(){
		N = 0;
	}

	void push(int val){
		q2.push(val);
		N++;

		while (!q1.empty()){
			q2.push(q1.front());
			q1.pop();
		}

		queue <int> temp = q1;
		q1 = q2;
		q2 = temp;
	}

	void pop(){
		q1.pop();
		N--;
	}

	int top(){
		return q1.front();
	}

	bool empty(){
		if (N == 0)
			return true;
		return false;
	}
};

// Method 2 --- in this pop function is costly
class Queue1{
	int N;
	queue<int> q1;
	queue<int> q2;
public:

	Queue1(){
		N = 0;
	}

	void push(int val){
		q1.push(val);
		N++;
	}

	void pop(){
		if (q1.empty()){
			cout<<"Underflow"<<endl;
			return;
		}

		while (q1.size() != 1){
			q2.push(q1.front());
			q1.pop();
		}
		q1.pop();
		N--;

		queue<int> temp = q1;
		q1 = q2;
		q2 = temp;
	}

	int top(){
		if (q1.empty()){
			return -1;
		}
		while (q1.size() != 1){
			q2.push(q1.front());
			q1.pop();
		}

		int ans = q1.front();
		q2.push(ans);

		queue<int> temp = q1;
		q1 = q2;
		q2 = temp;

		return ans;
	}

	int size(){
		return N;
	}
};

int main(){

	Queue1 st;
	st.push(1);
	st.push(2);
	st.push(3);
	st.push(4);
	st.push(5);

	cout<<st.top()<<endl;
	st.pop();

	cout<<st.top()<<endl;
	st.pop();

	cout<<st.size()<<endl;


	return 0;
}