#include <iostream>
#include <filesystem>
namespace fs = std::filesystem;
void dirn(std::string dir){
  if (is_directory(dir)){
    std::cout << "Is a directory" << endl;
    exit(0);
  }
}
