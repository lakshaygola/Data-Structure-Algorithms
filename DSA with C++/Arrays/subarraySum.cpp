#include "bits/stdc++.h"

using namespace std;

// Function to perform solution
void sumSubarrays(int nums[], int size, int s){
	int sum= 0, i=0, j=0, flag=0;

	while(j<size && sum+nums[j] <= s){
		sum += nums[j];
		j++;
	}

	if (sum == s){
		flag= 1;
		cout<<i+1<<" "<<j<<endl;
		return ;
	}

	while(j<size){
		sum += nums[j];
		while(sum > s){
			sum -= nums[i];
			i++;
		}
		if (sum == s){
			flag=1;
			i= i+1;
			j= j+1;
			cout<<i<<" "<<j<<endl;
			break;
		}
		j++;
	}

	if (flag == 0){
		cout<<"-1"<<endl;
	}
}

int main(){

	// test case 1
	int nums1[]= {1,2,3,8};
	int size1= sizeof(nums1)/sizeof(nums1[0]);
	int s= 5;
	sumSubarrays(nums1, size1, s);

	// test case 2
	int nums2[]= {12,45,87,45,3,1,56};
	int size2= sizeof(nums2)/sizeof(nums2[0]);
	int s2 = 100000;
	sumSubarrays(nums2, size2, s2);

	// test case 3
	int nums3[]= {1,2,3,7,5};
	int size3= sizeof(nums3)/sizeof(nums3[0]);
	int s3 = 12;
	sumSubarrays(nums3, size3, s3);

	return 0;
}