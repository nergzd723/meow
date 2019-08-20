#include <iostream>
#include <string>
#include "modulelist.h"

using namespace std;

void getenv(const string & var){
    const char* val = ::getenv(var.c_str());
    cout << val << endl;
    exit(0);
}
int checkforvar(string main){
    char doll;
    doll << main.at(1);
    cout << doll;
    if (doll == '$'){
        getenv(main);
    }
    return 0;
}
