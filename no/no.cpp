// Meow part
// NO:  GNU yes analog
// Copyright 2019, Oleg Sazonov(@x0r3d) in collaboration with Mark Hargreaves(@nergzd723)
// 13.09.19 nergzd723 fix error
#include <iostream>
#include <csignal>
#include <cstring>
#include "../external_projects/argh/argh.h"

using namespace std;
void helper(void) {
  cout << "NO: GNU yes analog" << endl;
  cout << "Usage: simply run this without help argh" << endl;
  cout << "OPTIONS: " << endl;
  cout << "-y,--yes                     floods yes(by default it's floods by no)";
  cout << "-h,--help                    print this message" << endl;
};
int main(int argc, char *argv[]) {
  argh::parser cmdl(argv);
  bool is_yes;
  if(cmdl[{"-y", "--yes"}]) {
    is_yes = true;
  } else {
    is_yes = false;
  };
  if(cmdl[{"-h", "--help"}]) {
    helper();
    return 0;
  }
  if(is_yes) {
    while(true) {
      cout << "yes" << endl;
    };
  } else {
    while(true) {
    cout << "no" << endl;
    };
  };
  return 0;
}
