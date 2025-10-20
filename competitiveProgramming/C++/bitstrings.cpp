#include <bits/stdc++.h>
using namespace std;

typedef long long longer;
const long long MOD = 1e9 + 7;


longer andrew(longer base, longer exp, longer mod){
    while(exp > 0){
        longer temp = base;
        base = base*base;
        if (exp % 2 == 1){
            base = base * temp;
        }
        exp = exp/2;
    }
    cout << base; 
}

long long fast_pow(long long base, long long exp, long long mod){
    long long result = 1;                       // result
    long long b = base % mod;                   // we use mod to limit 1e9 + 7;
    while(exp > 0){                             // exp is !0
        if (exp % 2 == 1){                      // if odd
            result = (result * b) % mod;        // result times bas,and limit using mod
        }     
        b = (b * b) % mod;                      // square the base
        exp /= 2;                               // half the expenonent
    }
    return result;
}

int main() {
    long long n;
    cin >> n;
    cout << fast_pow(2, n, MOD) << "\n";
    cout << simple_pow(2, n, MOD) << "\n";
    return 0;
}



int result = 1;
while(n > 0){
    result = (result * base ) % mod
}