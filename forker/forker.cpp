//Meow part
// Forker: gen new processes
// Copyright 2019, Oleg Sazonov(@x0r3d) in collaboration with Mark Hargreaves(@nergzd723)
// 12.09.19: Initial write
#include <iostream>
#include <unistd.h>
#include <thread>

using namespace std;

void fork_function(const char *command) {
  thread thr(system, command);
  thr.detach();
}

int main(int argc, char *argv[]) {
  if(argc == 1) {
    cout << "Forker: gen new processes" << endl;
    cout << "Usage: forker path_to_binary count_of_forks" << endl;
    return 0;
  }
  int count = atoi(argv[2]);
  int i;
  while(i < count) {
    fork_function(argv[1]);
    ++i;
  }

  return 0;
}
