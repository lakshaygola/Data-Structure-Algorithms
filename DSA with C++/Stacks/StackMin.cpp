/* Design the stack such that on calling min function it will return the minimum element 
of the stack in O(1) time */

#include "bits/stdc++.h"

using namespace std;

// class to define the stack which have min value function
class Stack{
    int *arr;
    int ptr;
    int size;
    int *minVal;
    int minIdx;

public:
    Stack(int n){
        arr = new int [n];
        ptr = -1;
        size = n;
        minVal = new int [n/2];
        minIdx = -1;
    }

    // Function to return the top value of the stack
    int top(){
        if (ptr == -1){
            return  -1;
        }
        return arr[ptr];
    }

    // Function to push the values in the stack
    void push(int val){
        if (ptr == size - 1){
            cout<<"OverFlow! NO MORE SPACE"<<endl;
            return;
        }
        int perVal = top();
        //cout<<"top values: "<<perVal;
        if (perVal == -1 or val < perVal){
            minIdx++;
            minVal[minIdx] = val;
            //cout<<" min values till now: "<<minVal[minIdx]<<endl; 
        }
        ptr++;
        arr[ptr] = val;
    }
    
    // Function to pop the value from the stack
    void pop(){
        if (ptr == -1){
            cout<<"No More Element"<<endl;
            return;
        }
        if (arr[ptr] == minVal[minIdx]){
            ptr--;
            minIdx--;
        }else
            ptr--;  
    }

    // Function to return the minimum element from the stack
    int min(){
        if (ptr == -1){
            cout<<"No More Elements"<<endl;
            return -1;
        }
        return minVal[minIdx];
    }

    // Function to find the empty stack
    bool empty(){
        if (ptr == -1)
            return true;
        return false;
    }
};

// Function to print the stack
void print(Stack st){
    while (!st.empty()){
        int val = st.top();
        st.pop();
        cout<<val<<endl;
    }
}

int main(){
    Stack st(10);

    st.push(5);
    st.push(6);
    st.push(3);
    st.push(10);
    st.push(1);

    print(st);


    cout<<"First "<<st.min()<<endl;
    st.pop();
    cout<<"Second "<<st.min()<<endl;
    st.pop();
    cout<<"Thrid "<<st.min()<<endl;
    st.pop();
    cout<<"Forth "<<st.min()<<endl;

    return 0;
}