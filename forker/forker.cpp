//Meow part
// Forker: gen new processes
// Copyright 2019, Oleg Sazonov(@x0r3d) in collaboration with Mark Hargreaves(@nergzd723)
// 12.09.19: Initial write
#include <iostream>
#include <unistd.h>
#include <fstream>

using namespace std;

__pid_t fork_function(const char *command) {
  __pid_t pid;
  system(command);
  pid = fork();
  return pid;
}

int main(int argc, char *argv[]) {
  if(argc == 1) {
    cout << "Forker: gen new processes" << endl;
    cout << "Usage: forker path_to_binary count_of_forks" << endl;
    return 0;
  }
  int count = atoi(argv[2]);
  int i;
  ofstream fout("forker.txt");
  for(int i; i < count; i++) {
    fout << "Created fork with pid: " << fork_function(argv[1]) << endl;
  }


  fout.close();
  return 0;
}
