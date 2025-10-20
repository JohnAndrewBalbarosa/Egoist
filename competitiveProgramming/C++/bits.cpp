#include <bits/stdc++.h>
using namespace std;
 
int main()
{
    int loop = 0;
    string input = "";
    int answer = 0;
    cin >> loop;
    while(loop--){
        cin.ignore();
        getline(cin, input);
        for(char c: input){
            if(c == '+'){
                answer++;
                break;
            }
            else if(c == '-'){
                answer--;
                break;
            }
        }
    }
    cout << answer;
    return 0;
}