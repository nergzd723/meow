#include <iostream>
#include <fstream>
#include <string>
#include "modulelist.h"

using namespace std;

int main (int argc, char **argv)
{
  if(argc == 1) {
    cout << "Meow: cat analog" << endl;
    cout << "Usage: meow file_to_meow(or environment variable)" << endl;
    return 0;
  }
    string buffer;
    ifstream filetomeow;
    filetomeow.open(argv[1]);
    if (!filetomeow.is_open()){
        string env = "";
        env = checkforvar(argv[1]);
        cout << env << endl;
        loopwait();                                 //if nothing worked, enter endless loop of repeating what user typed
        return 0;
    }
    while (getline(filetomeow, buffer)){                //main piece of code that inputs what did it get
        cout << buffer << endl;
    }
}
