#include <iostream>
#include <bits/stdc++.h>
using namespace std;
 
int checker(int size){
    int iter = 0, answer;
    for (int i = 0; i < 3; i++){
        cin >> answer;
        iter += answer;
    }
    if (iter >= 2){
        return 1;
    }
    return 0;
}
 
int main()
{
    int iter, size, answer = 0;
    cin >> size;
    iter = size;
    while(iter--){
        answer += checker(size);
    }
    cout << answer;
    
    return 0;
}