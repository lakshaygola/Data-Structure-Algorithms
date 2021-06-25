/* In this notebook we will evaluate the postfix expression
For example  --- 46+2/5*7+
Answer --- 32 */

#include "bits/stdc++.h"

using namespace std;

// Function to evaluate the post fix expression
int postEvaluation(string s){

	stack<int> st;

	for (int i=0; i<s.length(); i++){
		if (s[i] >= '0' && s[i] <= '9')
			st.push(s[i] - '0');
		else{
			int op1 = st.top();
			st.pop();
			int op2 = st.top();
			st.pop();

			switch(s[i]){
				case '+' : 
					st.push(op2+op1);
					break;
				case '-' :
					st.push(op2-op1);
					break;
				case '*' : 
					st.push(op2*op1);
					break;
				case '/' : 
					st.push(op2/op1);
					break;
				case '^' : 
					st.push(pow(op2, op1));
					break;
				default : 
					break;
			}`
		}
	}

	return st.top();
}


int main(){
	cout<<"Result of postfix: "<<postEvaluation("46+2/5*7+")<<endl;

	return 0;
}