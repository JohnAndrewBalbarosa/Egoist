#include <iostream>
#include <cstdint>
#include <string>
using namespace std;
 
int main()
{
    uint16_t k;
    cin >> k;
    cin.ignore();
    
    string l;
    uint16_t size; 
    
    while (k--) {
        getline(cin, l);
        size = l.length();
        if (size > 10) {
            cout << l[0] << size - 2 << l[size - 1] << endl; 
        }
        else {
            cout << l << endl;
        }
    }
    
    return 0;
}
