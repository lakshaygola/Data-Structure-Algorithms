/* Reverse the given string 
for e.g. - str --- "lakshay"
		   output -- "yahskal"*/

#include "bits/stdc++.h"

using namespace std;

// Function to reverse the given string
void ReverseString(string s){
	if (s.length() == 0)
		return;
	ReverseString(s.substr(1));
	cout<<s[0];
}

int main(){

	string str;
	cin>>str;

	ReverseString(str);
	cout<<endl;

	return 0;
}