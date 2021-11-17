/* Implement the stack of set in which if one stack extended the some threshold values 
then new stack will be created. But all together they should work as a single stack 
Implement popAt function which perform deletion from specific stack */

#include "bits/stdc++.h"

using namespace std;

// Class to define the structure of set of stacks
class setOfStacks{
    int *arr;
    int top;
    int size;
    int noOfStacks;

public:
    setOfStacks(int thersholdVal){
        size = thersholdVal;
        top = -1;
        arr = new int[size];
        noOfStacks = 1;
    }

    // Function to resize the current stack if threshold increases
    void resize(){
        noOfStacks++;
        int newSize = size * 2;
        int *newArr = new int[newSize];

        memcpy(newArr, arr, size * sizeof(int));

        size = newSize;
        delete [] arr;
        arr = newArr;
    }

    // Function to push the element in the stack
    void push(int val){
        if (top == size - 1){
            resize();
            top++;
            arr[top] = val;
        }else{
            top++;
            arr[top] = val;
        }
    }
    
    // Function to pop the element from the stack
    void pop(){
        if (top == -1){
            cout<<"NO MORE ELEMENTS"<<endl;
            return;
        }
        top--;
    }

    // Check for empty stack
    bool empty(){
        if (top == -1)
            return true;
        return false;
    }
    
    // Function to return the top value
    int FirstValue(){
        if (top == -1)
            return -1;
        return arr[top];
    }

    // Function to pop the element from the given stack
    int popAt(int stackNo){
        if (top == -1){
            return -1;
        }
        if (stackNo > noOfStacks){
            return -1;
        }else if (stackNo == noOfStacks){
            return arr[top];
        }else{
            return arr[(size * stackNo) -1];
        }
    }
};

// Function to print the stack
void print(setOfStacks st){
    while (!st.empty()){
        int val = st.FirstValue();
        st.pop();
        cout<<val<<endl;
    }
}

int main(){
    setOfStacks st(1);

    st.push(14);
    st.push(15);
    st.push(16);
    st.push(1);
    st.push(2);
    st.push(3);

    print(st);

    cout<<st.popAt(1);

    // cout<<st.FirstValue()<<endl;
    // st.pop();
    // cout<<st.FirstValue()<<endl;
    // st.pop();
    // cout<<st.FirstValue()<<endl;
    // st.pop();
    // cout<<st.FirstValue()<<endl;
    // st.pop();
    // cout<<st.FirstValue()<<endl;

    return 0;
}