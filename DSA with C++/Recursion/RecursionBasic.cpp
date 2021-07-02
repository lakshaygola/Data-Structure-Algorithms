/* Basic Recursion programs which can be helpful to understand the 
recursion better */

#include "bits/stdc++.h"

using namespace std;

// Function to print the factorial of the number 
int factorical(int n){
	if (n == 0)
		return 1;
	return n * factorical(n-1);
}

// Function to print the n fibonacci number
int nFib(int n){
	if (n == 0)
		return 0;
	else if (n == 1)
		return 1;
	return nFib(n-2) + nFib(n-1); 
}
   

int main(){

	int num;
	cin>>num;

	cout<<"Factorial of the "<<num<<" is: "<<nFib(num)<<endl;

	return 0;
}