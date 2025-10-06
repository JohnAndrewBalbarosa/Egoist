#include <iostream>
#include <climits>
#include "function.h"
using namespace std;

namespace arrGen {
    int** copyMatrix(int **matrix, int n) {
        int **matCopy = new int*[n];
        for (int i = 0; i < n; i++){
            matCopy[i] = new int[n];
            for (int j = 0; j < n; j++){
                matCopy[i][j] = matrix[i][j];
            }
        }
        return matCopy;
    }
}

void routeFinder::Activate(vector<route> &routeList){
    int cnt = 1, src = 0;
    for(route &router: routeList){
        cout << "[" << cnt << "] " << router.routeName << endl;
        cnt++;
    }
    cout << "Enter Route: ";
    cin >> cnt;
    clearScreen();
    
    cout << "Enter Source" << endl;
    for (int i = 0; i < routeList[cnt - 1].arraySize; i++){
        cout << "Source " << i << endl;
    }
    cin >> src;
    clearScreen();
    dijkstra(routeList[cnt - 1].matrix, src, routeList[cnt - 1].arraySize);
}

void routeFinder::dijkstra(int **matrix, int src, int numVertex) {
    int* distanceArr = new int[numVertex];
    for (int i = 0; i < numVertex; i++) {
        distanceArr[i] = INT_MAX;
    }
    distanceArr[src] = 0;
    
    int* predecessor = new int[numVertex];
    for (int i = 0; i < numVertex; i++) {
        predecessor[i] = -1; 
    }
    
    bool *visitedArr = new bool[numVertex];
    for (int i = 0; i < numVertex; i++) {
        visitedArr[i] = false;
    }
    
    for (int count = 0; count < numVertex - 1; count++) {
        int minValue = INT_MAX, currentVertex = -1;
        for (int i = 0; i < numVertex; i++) {
            if (!visitedArr[i] && distanceArr[i] < minValue) {
                minValue = distanceArr[i];
                currentVertex = i;
            }
        }
        
        if (currentVertex == -1)
            break; 
            
        visitedArr[currentVertex] = true;

        for (int v = 0; v < numVertex; v++) {
            if (!visitedArr[v] && 
                matrix[currentVertex][v] != -1 &&    // Only process valid connections
                distanceArr[currentVertex] != INT_MAX &&
                distanceArr[currentVertex] + matrix[currentVertex][v] < distanceArr[v]) {
                    distanceArr[v] = distanceArr[currentVertex] + matrix[currentVertex][v];
                    predecessor[v] = currentVertex;
            }
        }
    }

    cout << "Vertex \t Distance from Source \t Last Node" << endl;
    for (int i = 0; i < numVertex; i++) {
        cout << i << " \t\t " << distanceArr[i] << " \t\t ";
        if(predecessor[i] == -1)
            cout << "None";
        else
            cout << predecessor[i];
        cout << endl;
    }
    
    delete[] visitedArr;
    delete[] distanceArr;
    delete[] predecessor;
}
