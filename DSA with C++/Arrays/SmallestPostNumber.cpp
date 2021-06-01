#include "bits/stdc++.h"

using namespace std;

void smalledPosNumber(int nums[], int size){
	const int N= 1e6 + 2; 
	int ans, i;
	bool present[N];

	for(i=0; i<N; i++){
		present[i]= false;
	}

	for (i=0; i<size; i++){
		if (nums[i] >= 0){
			present[nums[i]] = true;
		}
	}
	for(i=0; i<N; i++){
		if (present[i] == false){
			ans= i;
			break;
		}
	}
	cout<<i<<endl;
}

int main(){
	// test case 1
	int nums1[]= {0,-9,1,3,-4,5};
	int size1= sizeof(nums1)/sizeof(nums1[0]);
	smalledPosNumber(nums1, size1);

	//test case 2
	int nums2[]= {0,1,2,-8,3,6,5,4,-8,-10,11};
	int size2= sizeof(nums2)/sizeof(nums2[0]);
	smalledPosNumber(nums2, size2);

	return 0;
}