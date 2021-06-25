/* We have the string which conatin the expression we have to find 
out the redundant parenthesis or extra parenthesis
for example -- ((a+b))  - output - 1(Contain the extra parenthesis)
		- (a+ (a+b)) - output - 0(Contain the no extra parenthesis)*/

#include "bits/stdc++.h"

using namespace std;

// Function to calculate th number of extra parenthesis
int redundantParenthesis(string c, int size){
	int ans = 0;

	stack <char> ch;

	for  (int i=0; i<size; i++){

		if (c[i] == '+' or c[i] == '-' or c[i] == '*' or c[i] == '/'){
			ch.push(c[i]);
		}

		else if (c[i] == '('){
			ch.push(c[i]);
		}

		else if (c[i] == ')'){

			if (ch.top() == '('){
				ans++;
			}

			while (ch.top()=='+' or ch.top()=='-' or ch.top()=='*' or ch.top()=='/'){
				ch.pop();
			}

			ch.pop();
		}
	}

	return ans;
}

int main(){

	string s;
	cin>>s;

	int size = s.size(); 
	
	cout<<"Extra parenthesis: "<<redundantParenthesis(s, size)<<endl;
	return 0;
}