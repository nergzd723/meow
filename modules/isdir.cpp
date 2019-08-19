using namespace std;

void main(char* dir){

  char *myDir = dirname(myPath);
  struct stat myStat;
  if ((stat(myDir, &myStat) == 0) && (((myStat.st_mode) & S_IFMT) == S_IFDIR)) {
      cout << "is a directory" << endl;
      exit(1)
  }
}
