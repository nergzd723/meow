#include <fstream>
#include <iostream>
#include <string>

using namespace std;

string inline checkforvar(const string &key) {
  char *val;
  val = getenv(key.c_str());
  string retval = "";
  if (val != NULL) {
    retval = val;
  }
  return retval;
}
int main(int argc, char **argv) {
  if (argc == 1) {
    cout << "Meow: cat analog" << endl;
    cout << "Usage: meow file_to_meow(or environment variable)" << endl;
    return 0;
  }

  ifstream filetomeow;
  filetomeow.open(argv[1]);
  if (!filetomeow.is_open()) {
    string env = "";
    env = checkforvar(argv[1]);
    cout << env << endl;
  }
  string buffer;
  while (getline(filetomeow,
                 buffer)) { // main piece of code that inputs what did it get
    cout << buffer << endl;
  }
  return 0;
}
