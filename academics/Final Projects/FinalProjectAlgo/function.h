#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include "data.h"
#include <queue>
#include <vector>
using namespace std;

class Interface {
public:
    void Starting(vector<route> &);
    static void clearScreen();
private:
    void mainMenu(int &);
};

class routeMenu { 
public:
    void Starting(vector<route> &);
    static void clearScreen();
private:
    void mainMenu(int &);
    void addRoute(vector<route> &);
    void addNode(route &, int);
    void changeNode(route &);
    void changer(vector<route> &);
    void generateMatrix(route &, int);
};

class routeFinder {
public:
    void Activate(vector <route> &);
    static void clearScreen();
private:
    void dijkstra(int** , int, int);
};

class passenger{
    public:
        void Starting(vector <route> &);
    private:
        void quickSort(vector<PassengerGroup>& groups, int low, int high);
        int partition(vector<PassengerGroup>&, int, int);
        void showMenu(vector<PassengerGroup>&);

};

#endif
