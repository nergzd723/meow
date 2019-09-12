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
  bool is_yes;
  if(argc == 1) is_yes = false;
  if(strcmp(argv[1], "-h")) {
    cout << "NO: GNU yes analog" << endl;
    cout << "Usage: no [OPTIONS]" << endl;
    cout << "Options:" << endl;
    cout << "-y            flood by yes(floods no by default)" << endl;
    return 0;
  };
  if(!strcmp(argv[1], "-y")) {
    is_yes = true;
  };

try{
  if(is_yes == false) {
    while(true) {
      signal(SIGINT,ctrl_handler);
      cout << "no" << endl;
    }
  } else {
    while(true) {
      signal(SIGINT,ctrl_handler);
      cout << "yes" << endl;
    }
  }
} catch(int a) {
  cout << "Got ctrl-c!" << endl;
  return 0;
}
}
