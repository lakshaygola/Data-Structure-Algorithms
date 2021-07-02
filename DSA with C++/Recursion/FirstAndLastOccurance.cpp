/* For the given array we have to find out the first occurance and the
last occurance of the particular element 
For example - arr --- [7,2,5,4,2,3,6,2,4], number --- 2
output --- (1,7) first 2 at 1st and the last 2 at 7th index*/

#include "bits/stdc++.h"

using namespace std;

// Function to find the first occurance of the number
int firstOccur(int a[], int size, int idx, int key){

	if (idx > size)
		return -1;

	if (a[idx] == key)
		return idx;

	return firstOccur(a, size, idx+1, key);
}

// Function to find the last occurance of the number in the array
int lastOccur(int a[], int size, int idx, int key){
	if (idx > size)
		return -1;

	int restArr = lastOccur(a, size, idx+1, key);

	if (restArr != -1){
		return restArr;
	}
	else{
		if (a[idx] == key)
			return idx;
		else
			return -1;
	}
}


int main(){
	
	int size;
	cin>>size;

	int nums[size];
	for (int i = 0; i<size; i++){
		cin>>nums[i];
	}

	cout<<firstOccur(nums, size, 0, 2)<<endl;
	cout<<lastOccur(nums, size, 0, 2)<<endl;
	return 0; 
}