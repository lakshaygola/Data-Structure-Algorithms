/* Implement the function to use single array to implement three stack 
In this we are assume the stack of constant size */

#include "bits/stdc++.h"

using namespace std;

// Class to define the structure
class ThreeStacks{
    int noOfStacks;
    int *StackSize;
    int *values;
    int capcity;
public:
    // Constructure
    ThreeStacks(int noOfStack, int size){
        noOfStacks = noOfStack;
        StackSize = new int[noOfStacks];
        values = new int[noOfStacks * size];
        capcity = size;
    }

    // Function to push the element in the stack
    void pushStack(int stackNo, int val){
        if (StackSize[stackNo - 1] == capcity){
            cout<<"Stack is OverFlow!! NO MORE SPACE"<<endl;
            return;
        }
        int idx = indexOfStack(stackNo);
        values[idx+1] = val;
        StackSize[stackNo]++;
    }

    // Function to pop the element of the stack
    void pop(int stackNo){
        if (StackSize[stackNo] == 0){
            cout<<"No more elements are there"<<endl;
            return;
        }
        StackSize[stackNo]--;
    }

    // Function to get the top values of the stack
    int top(int stackNo){
        if (StackSize[stackNo] == 0){
            return -1;
        }
        int idx= indexOfStack(stackNo);
        return values[idx];
    }

    // To find the stack is empty or not
    bool empty(int stackNo){
        if (StackSize[stackNo] == 0)
            return true;
        return false;
    }

    // Function to find the top values index of the stack
    int indexOfStack(int stackNo){
        int offset = capcity * (stackNo - 1);
        int size = StackSize[stackNo];
        return offset + size - 1;
    }

    // Function to print the stack
    void print(int stackNo){
        if (StackSize[stackNo] == 0){
            cout<<"Stack is empty"<<endl;
        }
        while (!empty(stackNo)){
            int val = top(stackNo);
            cout<<val<<endl;
            pop(stackNo);
        }
}
};


int main(){
    ThreeStacks st(3, 5);

    st.pushStack(1, 5);
    st.pushStack(1, 4);
    st.pushStack(1, 3);
    st.pushStack(1, 2);
    
    st.pushStack(2, 10);
    st.pushStack(2, 50);
    st.pushStack(2, 77);

    st.print(2);

    return 0;
}