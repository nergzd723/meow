// Meow part
// AName: uname analog
// Copyright 2019, Oleg Sazonov(@x0r3d) in collaboration with Mark
// Hargreaves(@nergzd723) 12.09.19: Initial write 17.09.19: Rewrite to working
// state
#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
  ifstream cat;
  cat.open("/proc/version", ios_base::in);
  string out;
  getline(cat, out);
  cout << out << endl;
  return 0;
}
