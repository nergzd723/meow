// Meow part
// Copyright 2019, Oleg Sazonov(@x0r3d) in collaboration with Mark Hargreaves(@nergzd723)
// EXO : echo analog
// 27.08.19: Initial write
#include <iostream> // for IO management
#include <fstream> // for file management
#include <cstring> // for check on arguments
using namespace std;

int main(int argc, char *argv[]) {
    if(argc == 1) {
        cout << "EXO: Yet another echo analog" << endl;
        cout << "Usage: exo some_text [path_to_write]" << endl;
        return 0;
    };
    bool file_write = false;
    if(argc == 3) file_write = true;
    if(file_write == true) {
        ofstream fout(argv[4]);
        fout << argv[1] << endl;
        fout.close();
    } else {
        cout << argv[1] << endl;
    };
    return 0;
}
    
