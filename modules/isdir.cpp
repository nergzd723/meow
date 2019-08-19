using namespace std;
#include <iostream>
#include <filesystem>
void dirn(string dir){
  if (is_directory(dir)){
    cout << "Is a directory" << endl;
    exit(0)
  }
}
