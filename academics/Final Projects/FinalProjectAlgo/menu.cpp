#include <iostream>
#include "function.h"
using namespace std;

void clearScreenUtil() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

void Interface::Starting(vector<route> &listRoutes) {
    int choice = 0;
    do {
        mainMenu(choice);
        switch (choice) {
            case 0:
                cout << "Exiting the program. Goodbye!\n";
                return;
            case 1: {
                routeMenu Menu;
                Menu.Starting(listRoutes);
                break;
                }
            case 2: {
                passenger Menu;
                Menu.Starting(listRoutes);
                break;
                }
            case 3:
                cout << "https://youtu.be/NFDFj10WDnA?feature=shared";
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
                break;
        }
        cout << "\nPress Enter to continue...";
        cin.ignore(1000, '\n');
        cin.get();
        clearScreenUtil();
    } while (true);
}

void Interface::mainMenu(int &choice) {
    cout << "===== Travel Information System =====\n"
         << "1. Configure Routes\n"
         << "2. Tickts to be sold\n"
         << "3. Secret\n"
         << "0. Exit\n"
         << "\n:: ";
    cin >> choice;
    clearScreenUtil();
}



void routeMenu::clearScreen() {
    clearScreenUtil();
}

void routeFinder::clearScreen(){
    clearScreenUtil();
}

