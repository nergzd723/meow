#include <iostream>
#include <string>
#include "modulelist.h"
using namespace std;
int checkforvar(string main){
    char doll;
    doll << main.at(0);
    if (doll = '$'){
        cout << getenv(&main);
        return 1;
    }
    return 0;
}
