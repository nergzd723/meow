// Meow part
// Tap: my C++ touch on your file...
// Copyright 2019, Oleg Sazonov(@x0r3d) with Mark Hargreaves(@nergzd723)
// 13.10.19: Initial write
#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
  if (argc == 1) {
    cout << "Tap: GNU touch rewrite" << endl;
    cout << "Usage: tap file_for_tap" << endl;
    return 0;
  }
  ifstream re(argv[1], ios_base::in);
  if (!re.is_open()) {
    cout << "I can't to create file!(or edit!)" << endl;
    return 0;
  }
  re.close();
  return 0;
}