/* For the given array check weather the array is sorted in acsending
order or not 
For example --- arr - [1,2,3,4,5,6,7], output -- True(as it is sorted)*/

#include <bits/stdc++.h>

using namespace std;

// Function to check wheather array is sorted or not
bool checkArray(int arr[], int size){

	if (size == 1){
		return true;
	}
	return arr[0] < arr[1] and checkArray(arr+1, size-1);
}

// Function to print the n numbers in increasing order
void incresingN(int n){
	if (n == -1){
		return;
	}
	incresingN(n-1);
	cout<<(n)<<" ";
} 

// Function to print the n numbers in decresing order
void decreasingN(int n){
	if (n == -1)
		return;
	cout<<n<<" ";
	decreasingN(n-1);
}

int main(){
	int n;
	cin>>n;
	int start = 1;
	decreasingN(n);
	cout<<endl;
	incresingN(n);

	/* arr[n];

	for(int i = 0; i<n; i++){
		cin>>arr[i];
	}*/


	return 0;
}