//Meow part
// AName: uname analog
// Copyright 2019, Oleg Sazonov(@x0r3d) in collaboration with Mark Hargreaves(@nergzd723)
// 12.09.19: Initial write
// 17.09.19: Rewrite to working state
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]) {
    ifstream cat("/proc/version");
    string out;
    while (getline(cat, out)) {
        cout << out << endl;
    }
    return 0;
}
