// CPP program to make histogram of an array 
#include <bits/stdc++.h> 
using namespace std; 
  
void printHistogram(int arr[], int n) 
{ 
    int maxEle = *max_element(arr, arr + n); 
  
    for (int i = maxEle; i >= 0; i--) { 
        cout.width(2); 
        cout << right << i << " | "; 
        for (int j = 0; j < n; j++) { 
  
            // if array of element is greater 
            // then array it print x 
            if (arr[j] >= i) 
                cout << " x "; 
  
            // else print blank spaces 
            else
                cout << "   "; 
        } 
        cout << "\n"; 
    } 
  
    // print last line denoted by ---- 
    for (int i = 0; i < n + 3; i++) 
        cout << "---"; 
  
    cout << "\n"; 
    cout << "     "; 
  
    for (int i = 0; i < n; i++) { 
        cout.width(2); // width for a number 
        cout << right << arr[i] << " "; 
    } 
} 
  
// Driver code 
int main() 
{ 
    int arr[10] = { 10, 9, 12, 4, 5, 2, 
                    8, 5, 3, 1 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    printHistogram(arr, n); 
    return 0; 
} 