/* In this notebook we will evaluate the prefix expression and find
this final result of the prefix expression
For example ---  -+7*45+20
Final answer  --- 25 */

#include "bits/stdc++.h"

using namespace std;

// Function to evaluate the prefix evaluation
int prefixEvaluation(string s){

	stack<int> st;

	for (int i = s.length()-1; i>=0; i--){
		if (s[i] >= '0' && s[i] <='9')
			st.push(s[i]-'0');
		else{
			int op1 = st.top();
			st.pop();
			int op2 = st.top();
			st.pop();

			switch(s[i]){
				case '+' : 
					st.push(op1+op2);
					break;
				case '-' :
					st.push(op1-op2);
					break;
				case '*' : 
					st.push(op1*op2);
					break;
				case '/' : 
					st.push(op1/op2);
					break;
				case '^' : 
					st.push(pow(op1, op2));
					break;
				default : 
					break;
			}
		}
	}
	return st.top();
}

int main(){
	cout<<"Result: "<<prefixEvaluation("-+7*45+20")<<endl;
	return 0;
}