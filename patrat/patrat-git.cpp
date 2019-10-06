// Meow part
// Patrat-Git: swap patrat repo to git
// Copyright 2019, Oleg Sazonov(@x0r3d, writing) and Mark Hargreaves(@nergzd723, idea)
// 04.09.19: Initial write
#include <iostream>
#include <fstream>
#include <string>
#include <boost/filesystem.hpp>

using namespace std;
namespace boostf = boost::filesystem;
void get_repo_name(string &h) {
int t = h.find("/", 29);
h.erase(0, t + 1);
}
int main(int argc, char *argv[]) {
  if(argc == 1) {
    cout <<  "Patrat->git swapper" << endl;
    cout << "Usage: patrat-git git_repo_to_clone(run ONLY IN PATRAT REPO)" << endl;
    return 0;
  }
  ifstream f(".patrat/RATLOG");
  if(!f.is_open()) {
    cout << "You running not in patrat repo!" << endl;
    return 0;
  }
  string command_git = "git clone ";
  command_git += argv[1];
  system(command_git.c_str());
  get_repo_name(command_git);
  cout << command_git << endl;
  return 0;
}
