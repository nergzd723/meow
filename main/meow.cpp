#include <iostream>
#include <fstream>
#include "modulelist.h"
using namespace std;

int main
(int argc, char **argv){
    string buffer;
    ifstream filetomeow;
    filetomeow.open(argv[1]);
    if (!filetomeow.is_open()){
        cout << "No input file available\n";
        return 1;
    }
    while (getline(filetomeow, buffer)){
        cout << buffer << endl;
    }
}
