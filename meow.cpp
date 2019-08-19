#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main(int argc, char **argv){
    char buff[255];
    ifstream filetomeow;
    filetomeow.open(argv[1]);
    if (!filetomeow.is_open()){
        cout << "No input file available\n";
        return 1;
    }
    while (getline(filetomeow, buff)){
        cout << buff << endl;
    }
}
