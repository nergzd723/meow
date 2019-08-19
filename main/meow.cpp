#include <iostream>
#include <fstream>
#include <string>
#include "modulelist.h"

using namespace std;

int checkforvar
(string main){
    char doll;
    doll << main.at(1);
    cout << doll;
    if (doll = '$'){
        return 0;
    }
    return 0;
    }
int main
(int argc, char **argv){
    string buffer;
    ifstream filetomeow;
    filetomeow.open(argv[1]);
    cout << argv[1];
    if (!filetomeow.is_open()){
        int i = checkforvar(argv[1]);
        loopwait();                                 //if nothing worked, enter endless loop of repeating what user typed
        return 0;
    }
    while (getline(filetomeow, buffer)){                //main piece of code that inputs what did it get
        cout << buffer << endl;
    }
}
