#include <iostream>
#include <cstdint>
using namespace std;
 
int main()
{
    uint16_t k;
    cin >> k;
    
    if (k == 2){
        cout << "NO";
    }
    
    else if (k % 2 == 0){
        cout  << "YES";
    }
    
    else {
        cout << "NO";
    }
 
    return 0;
}