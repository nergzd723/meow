#include <iostream>
#include <filesystem>
namespace fs = std::filesystem;
void dirn(char[] dir){
  if (fs::is_directory(dir)){
    std::cout << "Is a directory" << std::endl;
    exit(0);
  }
}
