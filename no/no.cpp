// Meow part
// NO:  GNU yes analog
// Copyright 2019, Oleg Sazonov(@x0r3d) in collaboration with Mark Hargreaves(@nergzd723)
#include <iostream>
#include <csignal>
#include <cstring>

using namespace std;

void ctrl_handler(int s) {
  throw 1;
}

int main(int argc, char *argv[]) {
  while(true) {
    cout << "yes\n";
  }
}
