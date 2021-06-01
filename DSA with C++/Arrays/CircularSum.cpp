#include "bits/stdc++.h"

using namespace std;

// Function to find the kadane sum
int kadane(int arr[], int size){
	int current=0, maxSum=INT_MIN;
	for(int i=0; i<size; i++){
		current += arr[i];
		maxSum= max(maxSum, current);
		if (current < 0)
			current= 0;
	}
	return maxSum;
}

// function to find the subarray sum in circular array
void circularSum(int nums[], int size){
	int totalSum= 0;
	int wrapingSum=0, nonWrapingSum=0;

	nonWrapingSum= kadane(nums, size);

	for(int i=0; i<size; i++){
		totalSum += nums[i];
		nums[i]= -nums[i];
	}

	wrapingSum= totalSum + kadane(nums, size);

	cout<<wrapingSum<<endl;
}

int main(){

	// test case
	int nums1[]= {-1,4,-6,7,5,-4};
	int size1= sizeof(nums1)/sizeof(nums1[0]);
	circularSum(nums1, size1);

	int nums2[]= {4,-4,6,-6,10,-11,12};
	int size2= sizeof(nums2)/sizeof(nums2[0]);
	circularSum(nums2, size2);
	
	return 0;
}