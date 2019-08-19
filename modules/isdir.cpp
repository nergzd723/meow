using namespace std;
#include <iostream>

void main(string dir){

  char *myDir = dirname(dir);
  struct stat myStat;
  if ((stat(dir, &myStat) == 0) && (((myStat.st_mode) & S_IFMT) == S_IFDIR)) {
      cout << "is a directory" << endl;
      exit(1)
  }
}
