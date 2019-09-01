#include <iostream>
#include <boost/filesystem.hpp>

using namespace boost::filesystem;
using namespace std;

void dirn(path dir){
  if (is_directory(dir)){

    cout << "Is a directory" << endl;
    exit(0);
  }
}
