#include <iostream>
#include "data.h"
#include "function.h"
using namespace std;

void routeMenu::Starting(vector<route> &routeList) {
    int choice = 0;
    do {
        mainMenu(choice);
        switch (choice) {
            case 0:
                cout << "Exiting the program. Goodbye!\n";
                return;
            case 1:
                addRoute(routeList);
                break;
            case 2:
                changer(routeList);
                break;
            case 3:
                routeFinder activate;
                activate.Activate(routeList);
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
                break;
        }
        cout << "\nPress Enter to continue...";
        cin.ignore(1000, '\n'); 
        cin.get(); 
        clearScreen();
    } while (true);
}

void routeMenu::mainMenu(int &choice) {
    cout << "===== Row Minimization =====\n"
         << "1. Add New Route\n"
         << "2. Change Node Route\n"
         << "3. Find path\n"
         << "0. Exit\n"
         << "\n:: ";
    cin >> choice;
    clearScreen();
}

void routeMenu::addRoute(vector<route> &routeList) {
    int numNodes;
    route *newRoute = new route();
    cout << "Enter route name: ";
    cin >> newRoute->routeName;
    cout << "Enter number of Nodes: ";
    cin >> numNodes;
    newRoute->arraySize = numNodes;
    generateMatrix(*newRoute, numNodes);
    
    addNode(*newRoute, numNodes);
    
    routeList.push_back(*newRoute);
    }

void routeMenu::generateMatrix(route &newRoute, int n) {
    newRoute.matrix = new int*[n];
    for (int i = 0; i < n; i++){
        newRoute.matrix[i] = new int[n]();   
    }
}

void routeMenu::addNode(route &newRoute, int n) {
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (i == j){
                newRoute.matrix[i][j] = -1;
            } else if (newRoute.matrix[j][i] != 0) {
                continue;
            } else {
                cout << "Add distance from Node " << i << " to " << j << ": ";
                cin >> newRoute.matrix[i][j];
                newRoute.matrix[j][i] = newRoute.matrix[i][j];
            }
        }
    }
}

void routeMenu::changeNode(route &newRoute) {
    int numChanges, nodeStart, nodeEnd;
    cout << "Enter number of nodes to be changed: ";
    cin >> numChanges;
    for (int i = 0; i < numChanges; i++){
        cout << "Enter starting node: ";
        cin >> nodeStart;
        cout << "Enter ending node: ";
        cin >> nodeEnd;
        cout << "Enter value: ";
        cin >> newRoute.matrix[nodeStart][nodeEnd];
        newRoute.matrix[nodeEnd][nodeStart] = newRoute.matrix[nodeStart][nodeEnd];
    }
}

void routeMenu::changer(vector <route> &routeList) {
    int cnt = 1, choice;
    cout << "[1] Change node\n[2] Delete Route\n";
    cin >> choice;
    clearScreen();
    for(route &routes: routeList){
        cout << "[" << cnt << "] " << routes.routeName << endl;
    }
    cout << "Enter your route:\n";
    cin >> cnt;
    switch (choice){
        case 1:
            changeNode(routeList[cnt - 1]);
            break;
        case 2:
            routeList.erase(routeList.begin() + (cnt - 1));
            break;
        default:
            cout << "Wrong Input!\n";
            break;
    }
}