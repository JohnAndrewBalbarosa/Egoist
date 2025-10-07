#include<iostream>
#include<iomanip>
using namespace std;

void intro1(); // calling the intro function 
char choose(char let); // the choose function
void choose2();
void intro2(); // The greetings
void condo(); // The cout of the condos
void apartment(); // The cout f the apartments
void dorm(); // cout of the dorm

int main(){
    //naming the variables
    float budget;
    string username;
    char  opt, type;
    char a;
    
    //greetings
    intro1(); 
    cout << right << setw(30) << "Enter Username: "; 
    getline(cin,username);
    cout << endl;
    cout << right << setw(20) << "Hello " << username << "," << endl << endl;
    intro2();
    
    q: // the go to function to go back here

    cout << right << setw(33) << "Enter Your Budget: ";
    cin >> budget;
    if (budget <= 1000){ // if budget is too low
        cout << "\t      Budget is too low for inquiry\n";
    }
    else if (budget <= 5000){
        type = 'D'; 
        cout << "Your budget is too low. You can only afford the Dormitories \n\n";
    }
    else if (budget > 5000){ //if budget is above a certain threshold
        choose2();
        cin >> a;
        choose(a);
    } 
    else {
        cout << "wrong input"; 
    }
    switch(type){ // The Choosing of housing based on the preference of the user
        case 'C': case 'c':
            condo();
            break;
        case 'D': case 'd':
            dorm();
            break;
        case 'A': case 'a':
            apartment();
            break;
        }
        for (int i = 1; i <= 135; i++){ // The lne borders
                cout << "-";
            }
    cout << "\n[Y] - Yes \n" << "[N] - No \n" << " Do you wish to go back? "; // the option to go back to the budget function when needed
    cin >> opt;
    switch(opt){
        case 'y':
        case 'Y':
            goto q;
        case 'n':
        case 'N':
            return 0;
    }
}

void intro1(){ // the intro of the program

    for (int i = 1; i <= 135; i++){ // The lne borders
            cout << "-";
        }
        cout << endl;
    cout << " _    _                 _               _    _             _                       \n"
         << "| |  | |               (_)             | |  | |           | |                      \n"
         << "| |__| | ___  _   _ ___ _ _ __   __ _  | |__| |_   _ _ __ | |_ ___ _ __ ___        \n"
         << "|  __  |/ _ \\| | | / __| | '_ \\ / _` | |  __  | | | | '_ \\| __/ _ \\ '__/ __|   \n"
         << "| |  | | (_) | |_| \\__ \\ | | | | (_| | | |  | | |_| | | | | ||  __/ |  \\__ \\   \n"
         << "|_|  |_|\\___/ \\__,_|___/_|_| |_|\\__, | |_|  |_|\\__,_|_| |_|\\__\\___|_|  |___/ \n"
         << "                                 __/ |                                             \n"
         << "                                |___/                                              \n"; 
    for (int i = 1; i <= 135; i++){ // The lne borders
            cout << "-";
        }
        cout << endl;
}

void intro2(){ // a brief overview of the function
    cout << right << setw(45) << "Welcome to Housing Hunters!\n\n"; 
    cout << right << setw(15) << "\t\t\t   In this program We offer a variety of dorm and condominium options to fit your needs and budget."
    << "The dorms are perfect for those students who want a more\n"
    << "\t\t   traditional college experience or for those who doesn't have that much budget with them, while the condominiums are ideal for those who can spend more for a\n"
    << "\t\t   bit more privacy and independence, or if you want a more lavish lifestyle you can spend on apartments." << endl << endl;   
}
void choose2(){ // calling the void choose function 
    cout << "       .__                            \n"      
         << "  ____ |  |__   ____   ____  ______ ____   /\\ \n" 
         << "_/ ___\\|  |  \\ /  _ \\ /  _ \\/  ___// __ \\  \\/\n" 
         << "\\  \\___|   Y  (  <_> |  <_> )___ \\\\  ___/  /\\ \n"
         << " \\___  >___|  /\\____/ \\____/____  >\\___  > \\/ \n" 
         << "     \\/     \\/                  \\/     \\/     \n\n" 
         << right << setw(28) << "[C] for Condo\n"
         << right << setw(27) << "[D] for Dorm\n"
         << right << setw(34) << "[A] for Apartments\n\n"
         << right << setw(39) << "Please Choose a Housing: ";
}

char choose(char let){
    cout << endl;
    switch (let) { // The switch case calls the dorm(), condo(), and apartment() functions
        case 'd': case 'D':{
            dorm();
            break;
        }
        case 'c': case 'C':{
            condo();
            break;
        }
        case 'a': case 'A': {
            apartment();
            break;
        }
        default: {
            cout << right << setw(26) << "wrong input\n";       
        }
    }   
}

void condo(){ //Condominium list
    cout << left << setw(30) << "Condominium"
            << left << setw(15) << "Stars"
            << left << setw(30) << "Distance from FEU Tech"
            << left << setw(40) << "Address"
            << left << setw(30) << "Contact Details"
            << endl;
            for (int i = 1; i <= 135; i++){
                cout << "-";
            }
            cout << endl;
            cout << left << setw(30) << "Lindonburg Residences"
            << left << setw(15) << "4.1/5 (11)"
            << left << setw(30) << "300 meters or 4 minutes walk"
            << left << setw(40) << "691 M.V. Delos Santas St., Sampaloc"
            << left << setw(30) << "0917 815 5775"
            << endl;
            cout << left << setw(30) << "University Tower 4 - P. Noval"
            << left << setw(15) << "4.2/5 (100)"
            << left << setw(30) << "400 meters or 6 minutes"
            << left << setw(40) << "Padre Noval St, Sampaloc"
            << left << setw(30) << "0919 079 1675"
            << endl;
            cout << left << setw(30) << "Crown Tower University Belt"
            << left << setw(15) << "3.9/5 (99)"
            << left << setw(30) << "300 meters or 4 minutes"
            << left << setw(40) << "839 Tolentino St, Sampaloc"
            << left << setw(30) << "0917 582 5167"
            << endl;
            cout << left << setw(30) << "Grand Residences Espana 1"
            << left << setw(15) << "3.9/5 (97)"
            << left << setw(30) << "350 meters or 5 minutes"
            << left << setw(40) << "1202 España Blvd, Sampaloc"
            << left << setw(30) << "0917 539 6888"
            << endl;
            cout << left << setw(30) << "The ONE Santo Tomas"
            << left << setw(15) << "4.0/5 (158)"
            << left << setw(30) << "600 meters or 8 minutes"
            << left << setw(40) << "870 M.F. Jhocson, Sampaloc"
            << left << setw(30) << "0917 545 2222"
            << endl;
}

void dorm(){ //Dormitory list
    cout << left << setw(30) << "Dormitory"
            << left << setw(15) << "Rating"
            << left << setw(30) << "Distance from FEU Tech"
            << left << setw(40) << "Address"
            << left << setw(30) << "Contact Details"
            << endl;
            for (int i = 1; i <= 135; i++){
                cout << "-";
            }
            cout << endl;
            cout << left << setw(30) << "PJAC Dorm"
            << left << setw(15) << "5/5 (2)"
            << left << setw(30) << "220 meters or 3 minute walk"
            << left << setw(40) << "1015, 821 Loyola St., Sampaloc city"
            << left << setw(30) << "(028) 521 4399"
            << endl;
            cout << left << setw(30) << "Rosquin"
            << left << setw(15) << "3.6/5 (8)"
            << left << setw(30) << "280 meters or 4 minute walk"
            << left << setw(40) << "M.V. Delos Santos St., Sampaloc City"
            << left << setw(30) << "(028) 722 42860"
            << endl;
            cout << left << setw(30) << "DEL CARMEN DORMITORY"
            << left << setw(15) << "4.3/5 (6)"
            << left << setw(30) << "350 meters or 5 minute walk"
            << left << setw(40) << "680 MV Delos Santos St, Sampaloc"
            << left << setw(30) << "(028) 735 3237"
            << endl;
            cout << left << setw(30) << "Rosman II Dormitory"
            << left << setw(15) << "No Reviews"
            << left << setw(30) << "280 meters or 4 minute walk"
            << left << setw(40) << "758 San Sebastian St, Quiapo"
            << left << setw(30) << "(028) 241 0057"
            << endl;
            cout << left << setw(30) << "M Residences Dormitory"
            << left << setw(15) << "4.0/5 (59)"
            << left << setw(30) << "600 meters or 8 minute walk"
            << left << setw(40) << "851 Moret St, Sampaloc"
            << left << setw(30) << "0919 000 0398"
            << endl;
            cout << left << setw(30) << "Freedom Building"
            << left << setw(15) << "4.3/5 (4)"
            << left << setw(30) << "650 meters or 9 minute walk"
            << left << setw(40) << "2161 Recto Ave, Sampaloc"
            << left << setw(30) << "0917 552 1521"
            << endl;
            cout << left << setw(30) << "East Manila Dormitory"
            << left << setw(15) << "4.4/5 (14)"
            << left << setw(30) << "280 meters or 4 minute walk"
            << left << setw(40) << "Gastambibe St., Sampaloc city"
            << left << setw(30) << "(028) 516 9214"
            << endl; 
}

void apartment(){ //Apartments list
     cout   << left << setw(30) << "Apartments"
            << left << setw(15) << "Rating"
            << left << setw(30) << "Distance from FEU Tech"
            << left << setw(40) << "Address"
            << left << setw(30) << "Contact Details"
            << endl;
            for (int i = 1; i <= 135; i++){
                cout << "-";
            }
            cout << endl;
            cout << left << setw(30) << "Joaquin Residences"
            << left << setw(15) << "5/5 (2)"
            << left << setw(30) << "350 meters or 5 minute walk"
            << left << setw(40) << "660 Reten, Sampaloc, Manila"
            << left << setw(30) << "0917 862 0768"
            << endl;
            cout << left << setw(30) << "Torre Central"
            << left << setw(15) << "3.6/5 (8)"
            << left << setw(30) << "500 meters or 7 minute walk"
            << left << setw(40) << "JX4R+P6X Galicia St, Sampaloc, Manila"
            << left << setw(30) << "0930 873 1110"
            << endl;
            cout << left << setw(30) << "966 P. Paredes Apartments"
            << left << setw(15) << "No Reviews"
            << left << setw(30) << "280 meters or 4 minute walk"
            << left << setw(40) << "966 Padre Paredes St, Sampaloc, Manila"
            << left << setw(30) << "0916 992 1518"
            << endl; 
            cout << left << setw(30) << "Elm's Residences"
            << left << setw(15) << "No Reviews"
            << left << setw(30) << "450 meters or 6 minute walk"
            << left << setw(40) << "1213 San Antonio, Sampaloc"
            << left << setw(30) << "0918 907 3902"
            << endl; 
            cout << left << setw(30) << "Rosario Place"
            << left << setw(15) << "No Reviews"
            << left << setw(30) << "130 meters or 2 minute walk"
            << left << setw(40) << "JX3Q+MR7, Loyola St, Sampaloc, Manila"
            << left << setw(30) << "0906 595 9120"
            << endl;
}