using namespace std;
namespace fs = std::experimental::filesystem;
#include <iostream>
#include <experimental/filesystem>
void dirn(string dir){
  if (is_directory(dir)){
    cout << "Is a directory" << endl;
    exit(0)
  }
}
