#include <bits/stdc++.h>
using namespace std;

typedef long long longer;
const long long MOD = 1e9 + 7;

longer andrew(longer base, longer exp, longer mod){
    while(exp > 0){
        if (exp % 2 == 1){
            longer temp = base;
            base = base * temp ;
        }
        else{
            base = base*base;
        }
        exp = exp/2;
    }

    return base; 
    
}


int main() {
    long long n;
    cin >> n;
    cout << andrew(2, n, MOD) << "\n";
    return 0;
}
