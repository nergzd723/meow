//Meow part
// Forker: gen new processes
// Copyright 2019, Oleg Sazonov(@x0r3d) in collaboration with Mark Hargreaves(@nergzd723)
// 12.09.19: Initial write
#include <iostream>
#include <unistd.h>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]) {
  if(argc == 1) {
    cout << "Forker: gen new processes" << endl;
    cout << "Usage: forker path_to_binary count_of_forks" << endl;
    return 0;
  }
  int count = atoi(argv[2]);
  __pid_t pid[count];
  int i;
  ofstream fout("forker.txt");

    system(argv[1]);
while(i < count) {
  pid[i] = fork();
  fout << "Created fork with pid: " << pid[i] << endl;
}

  fout.close();
  return 0;
}
