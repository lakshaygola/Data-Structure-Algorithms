#include "bits/stdc++.h"

using namespace std;

// binary search approch
/*void sumPair(int nums[], int size, int value){
*/

// Function to find the pair
void pairSum(int nums[], int size, int value){
	int i=0, j=size-1;
	while (i<=j){

		if (nums[i]+nums[j] == value){ 
			cout<<"true"; 
			return ;
		}

		else if (nums[i]+nums[j] > value){ j--; }

		else{ i++; }
	}
	cout<<"false";
}

int main(){
	// test case 1
	int nums1[]= {2,4,7,11,14,16,20,21};
	int size1= sizeof(nums1)/sizeof(nums1[0]);
	int k= 31;
	pairSum(nums1, size1, k);

	return 0;
}


