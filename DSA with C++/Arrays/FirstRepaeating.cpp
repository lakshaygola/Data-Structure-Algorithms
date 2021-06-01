#include "bits/stdc++.h"

using namespace std;

// function to find the first repeating element (burte force)
void fre(int nums[], int size){
	int j, i, flag=0;
	for(i=0; i<size; i++){
		for (j=i+1; j<size; j++){
			if (nums[i] == nums[j]){
				flag = 1;
				break;
			}
		}
		if (flag == 1)
			break;
	}
	int ans = i+1;
	cout<<ans;
}

// Optimal solution 
void optimalFre(int nums[], int size){
	const int N = 1e6 + 2;
	int idx[N], minIdx= INT_MAX;
	
	for(int i=0; i<N; i++)
		idx[i] = -1;

	for(int i=0; i<size; i++){

		if (idx[nums[i]] != -1){
			minIdx= min(minIdx, idx[nums[i]]);
		}
		
		else{
			idx[nums[i]] = i;
		}	
	}	

	if (minIdx == INT_MAX){
		cout<<"-1"<<endl;
	}
	else{
		cout<< minIdx+1<<endl;
	}
}

int main(){
	// test case 1
	int nums1[] = {1,5,3,4,3,5,6};
	int size1 = sizeof(nums1)/sizeof(nums1[0]);
	optimalFre(nums1, size1);

	// test case 2
	int nums2[] = {1,5,3,85,69,45,2,15,7,9,63,3};
	int size2= sizeof(nums1)/sizeof(nums2[0]);
	optimalFre(nums2, size2);

	return 0;
}