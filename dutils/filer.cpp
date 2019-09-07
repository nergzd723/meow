//Filer util
//Creates some directories
//Testing purpoces only
//Mark Hargreaves and x0r3d
//Part of MEOW project

#include <filesystem>
#include <string>
#include <iostream>

using namespace std;
using namespace std::filesystem;

int main
(int argc, char *argv[])
{
  const path workdir = current_path();
  string dirs;
  cout << "How many directories to create? ";
  dirs << cin;
  int n = stoi(dirs);
  for (int i; i!=n; i++)
  {
    return 0;
    //not ready yet
  }
  
}


