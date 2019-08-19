#include <iostream>
#include <string>
#include "modulelist.h"
using namespace std;
int check(string main){
    char doll;
    doll << main.at(0);
    if (doll = '$'){
        return 1;
    }
    return 0;
}
