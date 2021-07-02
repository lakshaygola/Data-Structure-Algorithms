/* In the given string replace all the pi with its value that is 3.14
for e.g. - "pippxppixipi"
replace it with --- "3.14ppxp3.14xi3.14" */

#include "bits/stdc++.h"

using namespace std;

// Function to replace the pi with 3.14
void piReplacer(string s){
	if (s.length() == 0)
		return;

	if (s[0] == 'p' and s[1] == 'i'){
		cout<<"3.14"; 
		piReplacer(s.substr(2));
	}
	else{
		cout<<s[0];
		piReplacer(s.substr(1));
	}
}

int main(){

	string s;
	cin>>s;

	piReplacer(s);

	return 0;
}