/* We have a string which contain the different parenthesis we have
to check wheather the string is balance or not
Example - balance string  ----  "{[()]}" 
		  unbalance string ---  "{[(])}"  */

# include "bits/stdc++.h"

using namespace std;

// Function to find that string is balance or not
bool isbalance(string s){

	bool ans = true;
	stack <int> st;

	for (int i=0; i<s.length(); i++){
		if (s[i] == '(' || s[i] == '[' || s[i] == '{')
			st.push(s[i]);

		else if (s[i] == ')'){
			if (!st.empty() && st.top() == '(')
				st.pop();
			else
				return false;
		}

		else if (s[i] == ']'){
			if (!st.empty() && st.top() == '[')
				st.pop();
			else
				return false;
		}

		else if (s[i] == '}'){
			if (!st.empty() && st.top() == '{')
				st.pop();
			else
				return false;
		}
	}

	return true;
}

int main(){

	string s = "[{[([])]}]";

	if (isbalance(s))
		cout<<"string is balanced"<<endl;

	else
		cout<<"string is unbalanced"<<endl;

	return 0;
}