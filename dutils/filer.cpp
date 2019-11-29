//Filer util
//Creates some directories
//Testing purpoces only
//Mark Hargreaves and x0r3d
//Part of MEOW project

#include <filesystem>
#include <string>
#include <iostream>
#include <stdio.h>
#include <io.h>

using namespace std;
using namespace std::filesystem;

int main
(int argc, char *argv[])
{
  const path workdir = current_path();
  string dirs;
  cout << "How many directories to create? ";
  dirs << cin;
  int n = atoi(dirs);
  mkdir("ndir")
  while (n>0)
  {
    mkdir("")
    n--;
  }
  
  return 0;
}


