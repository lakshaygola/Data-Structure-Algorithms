#include "bits/stdc++.h"

using namespace std;

// Brute Force approch
void BruteMss(int nums[], int size){
	int maxSum= INT_MIN;

	for(int i=0; i<size; i++){
		for(int j=i; j<size; j++){
			int sum=0;
			for(int k=i; k<=j; k++){
				sum += nums[k];
			}	
			maxSum= max(maxSum, sum);
		}
	}
	cout<<maxSum<<endl;
}

// Function to print the maximum sum
void MaxiSubarraySum(int nums[], int size){
	int maxSum= INT_MIN;
	int sums[size+1]= {0};

	for(int i=1; i<=size; i++){
		sums[i]= sums[i-1] + nums[i-1];
	}
	int sum= 0;
	for(int i=1 ; i<=size; i++){
		for(int j=0; j<size; j++){
			sum= sums[i] - sums[j];
			maxSum= max(sum, maxSum); 
		}
	}
	cout<<maxSum<<endl;
}


// Most optimal solution (kadane's algorithms)
void optimalSum(int nums[], int size){
	int maxSum= INT_MIN;
	int currentSum= 0;

	for(int i=0; i<size; i++){
		currentSum += nums[i];
		maxSum= max(maxSum, currentSum);
		if (currentSum < 0)
			currentSum = 0;
	}

	cout<<maxSum<<endl;
}


int main(){
	// test case 1
	int nums1[]= {-1,4,7,2};
	int size1= sizeof(nums1)/sizeof(nums1[0]);
	optimalSum(nums1,size1);

	//test case 2
	int nums2[]= {1,2,7,9,12};
	int size2= sizeof(nums2)/sizeof(nums2[0]);
	optimalSum(nums2, size2);

	return 0;
}