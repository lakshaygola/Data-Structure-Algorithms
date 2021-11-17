/* Stack basic function */

#include "bits/stdc++.h"
using namespace std;

// Class to define the structure of the stack 
class Stack{
    int* arr;
    int ptr;
    int size;
    int* temp;
    int tempPtr;
public: 
    Stack(int n){
        arr = new int[size];
        temp = new int[size];
        tempPtr = -1;
        ptr = -1;
        size = n;
    }
    
    // Approch 1 - sort the stack while pushing the element into it
    // Function to implement the push function in the stack
    void push(int val){
        if (ptr == size-1){
            cout<<"Stack is overflow!! No More Space"<<endl;
            return;
        }
        int topVal = top();
        if (topVal == -1 or topVal > val){
            ptr++;
            arr[ptr] = val;
        }else if (topVal < val){
            do{
                pop();
                tempPtr++;
                temp[tempPtr] = topVal;
                topVal = top();
                if (topVal == -1){
                    break;
                }
            }while (topVal < val);
            ptr++;
            arr[ptr] = val;
            while (tempPtr != -1){
                topVal = temp[tempPtr];
                ptr++;
                arr[ptr] = topVal;
                tempPtr--;
            }
        }
    }

    // Function to perform pop function in the stack
    void pop(){
        if (ptr == -1){
            cout<<"No More Element In Stack"<<endl;
            return;
        }
        ptr--;
    }

    // Function to perform top function in the stack
    int top(){
        if (ptr == -1){
            return -1;
        }
        return arr[ptr];
    }

    // Function to perform empty function in the stack
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
        cout<<val<<endl;
        st.pop();
    }
}

int main(){
    Stack st (8);
    st.push(5);
    st.push(6);
    st.push(2);
    st.push(15);
    st.push(3);
    st.push(1);

    print(st);
    return 0;
}