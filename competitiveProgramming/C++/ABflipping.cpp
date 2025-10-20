#include <bits/stdc++.h>
using namespace std;

#define ll long long unsigned int

void AB(string &str, ll size){
    ll count = 0;
    bool looper = true;
    bool taken[size];
    ll left = 0;
    ll right = size - 2;
    for (ll i = 0; i < size; i++) {
        taken[i] = true;
    }

    if (size == 2) {
        if (str[0] == 'A' && str[1] =='B'){
            cout << "1" << endl;
            return;
        } else {
            cout << "0" << endl;
            return;
        }

    }
    while (looper) {
        looper = false;
        while (left <= right ) {
            if (str[right] == 'A' && str[right + 1] =='B' && taken[right]) {
                count++;
                swap(str[right], str[right + 1]);
                looper = true;
                taken[right] = false;
            }
            if (left == right) {
                break;
            }
            if (left != right) {
                right--;
            }


        }
        if (taken[left] == false) {
            left++;
        }
        if (taken[size - 2] == false) {
            size--;
        }
        right = size - 2;
    }
    cout << count << endl;
}

int main() {
    string str = "";
    ll input = 0;
    ll size = 0;
    cin >> input;
    while (input--) {
        cin >> size;
        cin.ignore();
        getline(cin, str);
        AB(str, size);
    }
    return 0;
}