#ifndef data_h
#define data_h

#include <string>
#include <utility>
#include <vector> 

using namespace std;

/*
Things I need:
    Matrix
    Pair array <- count for alloc can be done during the matrix creation 
    Route of traffic
    Maximum speed when no traffic
    Maximum speed when there is traffic
    
    |could be added later|
    name of route
*/
struct PassengerGroup {
    string groupName;
    int groupSize;
};

struct route {
    int **matrix;
    int arraySize;
    string routeName;
    vector<PassengerGroup> groups; 
};

#endif
