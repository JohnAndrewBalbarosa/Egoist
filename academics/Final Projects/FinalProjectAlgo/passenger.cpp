#include "data.h"       // Assumes PassengerGroup is defined here
#include "function.h"
#include <iostream>
#include <vector>
#include <string>
#include <utility>
using namespace std;

int passenger::partition(vector<PassengerGroup>& groups, int low, int high) {
    int pivot = groups[high].groupSize; 
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (groups[j].groupSize > pivot) {
            i++;
            swap(groups[i], groups[j]);
        }
    }
    swap(groups[i + 1], groups[high]);
    return i + 1;
}

void passenger::quickSort(vector<PassengerGroup>& groups, int low, int high) {
    if (low < high) {
        int pi = partition(groups, low, high);
        quickSort(groups, low, pi - 1);
        quickSort(groups, pi + 1, high);
    }
    
}

void passenger::Starting(vector<route> &routes) {
    int cnt;
    if (routes.empty()) {
        cout << "No routes available for passenger assignment." << endl;
        return;
    }
    
    for(route &router: routes){
        cout << "[" << cnt + 1 << "] " << router.routeName <<endl;
    }
    cout << "Enter Route: ";
    cin >> cnt;
    
    cout << "Passenger seating assignment for route: " << routes[cnt - 1].routeName << endl;
    
    if (routes[cnt - 1].groups.size() > 0){
        showMenu(routes[cnt - 1].groups);
        return;
    }
    
    vector<PassengerGroup> groups;
    int n;
    cout << "Enter number of passenger groups: ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        PassengerGroup pg;
        cout << "Enter group name: ";
        cin >> pg.groupName;
        cout << "Enter group size: ";
        cin >> pg.groupSize;
        groups.push_back(pg);
    }
    
    routes[cnt - 1].groups = groups;
    
    if (!groups.empty()) {
        quickSort(groups, 0, groups.size() - 1);
    }
    showMenu(groups);
}

void passenger::showMenu(vector<PassengerGroup> &groups){
    cout << "\nSeating Arrangement (Front to Back):" << endl;
    cout << "Seat No.\tGroup Name\tGroup Size" << endl;
    for (size_t i = 0; i < groups.size(); i++) {
        cout << (i + 1) << "\t\t" 
             << groups[i].groupName << "\t\t" 
             << groups[i].groupSize << endl;
    }
}