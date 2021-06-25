/* In this notebook will we convert the infix to postfix expression 
For example -- "(a-b/c)*(a/k-l)" 
Answer --- "abc/-ak/l-*" */

#include "bits/stdc++.h"

using namespace std;

// Helper Funciton to find the precedence of the current character
int prece(char c){
	
	if (c == '^')
		return 3;

	if (c == '*' || c == '/')
		return 2;

	if (c == '+' || c == '-')
		return 1;

	return -1;
}

// Function to convert the infix to postfix expression
string inToPrefix (string s){

	stack<int> st;
	string result;

	for (int i=0; i<s.length(); i++){
		
		if (s[i] == ')')
			st.push(s[i]);

		else if (!st.empty() && s[i] == '('){
			while (st.top() != ')'){
				result += st.top();
				st.pop();
			}
			if (!st.empty())
				st.pop();
		}

		else if ((s[i] >= 'a' && s[i] <='z') || (s[i] >= 'A' && s[i] <='Z')){
			result += s[i];
		}

		else{
			while (!st.empty() && prece(st.top()) > prece(s[i])){
				result += st.top();
				st.pop();
			}

			st.push(s[i]);
		}
	}

	while (!st.empty()){
		result += st.top();
		st.pop();
	}

	return result;
}

string infixToPrefix(string s){
	
	string result;

	reverse(s.begin(), s.end());
	result = inToPrefix(s);
	reverse(result.begin(), result.end());

	return result;
}

int main(){

	cout<<"Prefix Expression: "<<infixToPrefix("(a-b/c)*(a/k-l)")<<endl;

	return 0;
}