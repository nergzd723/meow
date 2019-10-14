// Meow part
// Tap: my C++ touch on your file...
// Copyright 2019, Oleg Sazonov(@x0r3d) with Mark Hargreaves(@nergzd723)
// 13.10.19: Initial write
#include <iostream>
#include <cstdio>

using namespace std;

int main(int argc, char *argv[]) {
    if(argc == 1) {
        cout << "Tap: GNU touch rewrite" << endl;
        cout << "Usage: tap file_for_tap" << endl;
        return 0;
    }
    FILE *re = fopen(argv[1], "w");
    if(!re) {
        cout << "I can't to create file!(or edit!)" << endl;
        return 0;
    }
    fclose(re);
    return 0;
}