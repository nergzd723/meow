#include <iostream>
#include <string>
#include "modulelist.h"

using namespace std;

int checkforvar(string main){
    char doll;
    doll << main.at(1);
    cout << doll;
    if (doll = '$'){
        return 0;
    }
    return 0;
}
