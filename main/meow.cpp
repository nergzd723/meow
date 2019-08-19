#include <iostream>
#include <fstream>
#include <string>
#include "modulelist.h"

using namespace std;

int main
(int argc, char **argv){
    string buffer;
    ifstream filetomeow;
    filetomeow.open(argv[1]);
    if (!filetomeow.is_open()){                     
        if (checkforvar(argv[1]) == 1){ 
            cout << getenv(argv[1]) << endl;            //if something go wrong, check is it envvar, if it is, read it
        }
        else{
        
            loopwait();                                 //if nothing worked, enter endless loop of repeating what user typed
        }
        return 0;
    }
    while (getline(filetomeow, buffer)){                //main piece of code that inputs what did it get
        cout << buffer << endl;
    }
}
